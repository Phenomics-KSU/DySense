# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import time
import zmq
import json
import traceback
import sys

from dysense.core.utility import make_unicode
from dysense.interfaces.client_interface import ClientInterface
from dysense.interfaces.component_connection import ComponentConnection
from dysense.core.version import s2c_version

class SensorBase(object):
    '''
    Base class for all sensor drivers.

    All sensor drivers written in python should inherit from this class. Most of its public interface
    is over a socket where inputs are time/commands and outputs are data/messages/status. The only
    public method is run() which handles everything.
    '''

    # The keys are the possible states the driver can be in.
    # The values are the 'health' associated with each state.
    possible_states = {'closed': 'neutral',
                       'waiting_for_time': 'neutral',
                       'normal': 'good',
                       'timed_out': 'bad',
                       'error': 'bad',
                       'bad_data_quality': 'bad'
                       }

    def __init__(self, sensor_id, instrument_id, context, connect_endpoint, desired_read_period=0.25, max_closing_time=2,
                 heartbeat_period=0.5, wait_for_valid_time=True, throttle_sensor_read=True, decide_timeout=True):
        '''
        Base constructor.

        Args:
            connect_endpoint - controller endpoint to connect to and get messages from.
            desired_read_period - the expected duration (in seconds) between sequential sensor reads.
            max_closing_time - maximum number of seconds sensor needs to wrap up before being force closed.
            heartbeat_period - How often (in seconds) we should receive a new message from controller and
                                 how often we should send one back.
        '''
        self.sensor_id = make_unicode(sensor_id)
        self.instrument_id = make_unicode(instrument_id)

        self.desired_read_period = max(0, desired_read_period)
        self.max_closing_time = max(0.1, max_closing_time)
        self.wait_for_valid_time = wait_for_valid_time
        self.throttle_sensor_read = throttle_sensor_read

        # If set to true then if the sensor base will determine if a time out is caused by the sensor actually timing out
        # or just returning to run the process loop.  This can be set to false if the sensor has multiple sources that come
        # in at different times and need to be monitored separately.
        self.decide_timeout = decide_timeout

        # Set to true when receive 'close' command from controller.
        self.received_close_request = False

        # Current sensor state. Private to keep in ensure controller is notified when changes.
        # The corresponding health can be requested from the health property.
        self._state = 'closed'

        # How often sensor reports new heartbeat.
        heartbeat_period = max(0.1, heartbeat_period)

        # How often the message receive loop in run() should be executed.
        self.main_loop_processing_period = min(heartbeat_period, 0.2)

        # How long the read_new_data() method is allowed to run without returning.
        # This assumes the request_new_data() method doesn't take very much time.
        self.max_read_new_data_period = self.main_loop_processing_period * .9

        # True if sensor shouldn't be saving/sending any data.
        self._paused = True

        # This is a flag that the read_new_data() method can use to track whether or not it needs to
        # request new data, or it's still waiting on data to come in.  The idea is the function can't
        # block for too long so it needs a way to track the state of the read between calls.
        self.still_waiting_for_data = False

        # Time references used to improve precision when sensor requests current time.
        self._last_received_sys_time = 0
        self._last_received_utc_time = 0

        # Where the controller wants to save data files.
        self.override_data_file_directory = None

        # If set to false then any directory specified by controller will be ignored.
        # Sensor driver can assign directory to this field.
        self.override_data_file_directory_allowed = True

        # Default location to store data files if one isn't set by controller.  Sensor driver
        # can assign directly to this field.
        self.default_data_file_directory = None

        # Associate callback methods with different message types.
        self.message_callbacks = {'command': self.handle_command,
                                  'time': self.handle_new_time,
                                  'change_setting': self.handle_change_setting}

        # The time to run next run each loop.  Used to figure out how long to wait after each run.
        self.next_processing_loop_start_time = 0
        self.next_sensor_loop_start_time = 0

        # System time that data was last received from the sensor.
        self.last_received_data_time = 0

        # How many message 'data' messages have been sent to controller.
        self.num_data_messages_sent = 0

        # System time when sensor was setup.
        self.sensor_setup_sys_time = 0

        # Setup interface used for communicating with controller.
        self.interface = ClientInterface(context, sensor_id, s2c_version)
        self.interface.register_callbacks(self.message_callbacks)
        self.interface.heartbeat_period = heartbeat_period
        self.interface.max_closing_duration = self.max_closing_time

        self.interface.wire_to_endpoint('controller', connect_endpoint)

        # Register connection instead of having one created automatically so can monitor it
        # easier and don't have to track server id (which is arbitrary anyways)
        self.controller_connection = ComponentConnection(self.interface, 'controller')
        self.interface.register_connection(self.controller_connection)

    @property
    def utc_time(self):
        '''Return current UTC time or 0 if haven't received a time yet.'''
        utc_time = self._last_received_utc_time
        if utc_time > 0:
            # Account for time that has elapsed since last time we received a time message.
            elapsed_time = self.sys_time - self._last_received_sys_time
            if elapsed_time > 0:
                utc_time += elapsed_time

        return utc_time

    @property
    def sys_time(self):
        '''Return current system time as a floating point number.'''
        return time.time()

    @property
    def state(self):
        '''Return the current sensor state.'''
        return self._state

    @state.setter
    def state(self, new_state):
        '''Update state and notify controller that they changed.'''
        if new_state not in SensorBase.possible_states:
            raise ValueError("Invalid sensor state {}".format(new_state))
        if new_state == self._state:
            return # don't keep sending out new status updates
        self._state = new_state
        self.send_status_update()

    @property
    def health(self):
        '''Return the health corresponding to the current sensor state.'''
        return SensorBase.possible_states[self.state]

    @property
    def paused(self):
        '''Return true if the sensor is currently paused.'''
        return self._paused

    @paused.setter
    def paused(self, new_value):
        '''Set paused to true/false and then notify controller that the status changed if it's different.'''
        if new_value == self._paused:
            return # don't keep sending out new status updates
        self._paused = new_value
        self.send_status_update()

    @property
    def current_data_file_directory(self):

        if self.override_data_file_directory and self.override_data_file_directory_allowed:
            data_file_directory = self.override_data_file_directory
        else:
            data_file_directory = self.default_data_file_directory

        return data_file_directory

    @property
    def seconds_since_sensor_setup(self):
        return self.sys_time - self.sensor_setup_sys_time

    def run(self):
        '''Set everything up, collect data and then close everything down when finished.'''
        try:
            # Setup ZMQ socket and then give sensor driver a chance to set itself up.
            self.interface.setup()
            self.send_status_update()
            self.setup()
            self.sensor_setup_sys_time = self.sys_time

            while True:

                if self._need_to_run_processing_loop():

                    # Save off time so we can limit how fast the loop runs.
                    self.next_processing_loop_start_time = self.sys_time + self.main_loop_processing_period

                    # Handle any messages received over ZMQ socket.
                    self.interface.process_new_messages()

                    if self.controller_connection.connection_state == 'timed_out':
                        raise Exception("Controller connection timed out.")

                    if self.received_close_request:
                        break # end main loop

                if self._need_to_run_sensor_loop():

                    if not self.still_waiting_for_data:
                        self.request_new_data()

                        # Save off time so we can limit how fast the loop runs.
                        self.next_sensor_loop_start_time = self.sys_time + self.desired_read_period

                    reported_state = self.read_new_data()

                    if reported_state == 'timed_out':
                        if self.should_have_new_reading() or not self.decide_timeout:
                            # Sensor actually did time out so we want to request new data.
                            self.still_waiting_for_data = False
                        else:
                            # Didn't actually time out.. just returned to process new controller messages.
                            reported_state = self.state
                            self.still_waiting_for_data = True
                    else:
                        # Not timed-out so not still waiting for data.
                        self.still_waiting_for_data = False

                    # If sensor is ok then override state if we're still waiting for a valid time.
                    reported_bad_state = SensorBase.possible_states[reported_state] == 'bad'
                    waiting_for_time = self.wait_for_valid_time and self.utc_time == 0
                    if not reported_bad_state and waiting_for_time:
                        reported_state = 'waiting_for_time'

                    self.state = reported_state

                # Figure out how long to wait before one of the loops needs to run again.
                # If not throttling sensor then the read_new_data() is in charge of waiting.
                if self.throttle_sensor_read and not self.still_waiting_for_data:
                    next_time_to_run = min(self.next_processing_loop_start_time, self.next_sensor_loop_start_time)
                    time_to_wait = next_time_to_run - self.sys_time
                    time.sleep(max(0, time_to_wait))

        except Exception as e:
            # Get information about exception
            exc_type, exc_value, exc_traceback = sys.exc_info()
            #formatted_exception = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
            formatted_lines = traceback.format_exc().splitlines()
            traceback_lines = formatted_lines[:-1]

            self.state = 'error'
            self.send_text("------------")
            self.send_text("{} - {}".format(type(e).__name__, make_unicode(e)))
            for traceback_line in traceback_lines:
                self.send_text(traceback_line)
            self.send_text("------------")
        finally:
            if self.health != 'bad':
                # The closed state is only for when things closed down on request... not because an error occurred.
                self.state = 'closed'
            self.received_close_request = False
            self.send_event('closing')
            self.paused = True
            self.pause()
            self.close()
            self.interface.close()

    def close(self):
        '''Stop reading sensor data and close down any resources. Sensor must override.'''
        raise NotImplementedError

    def is_closed(self):
        '''Return true if sensor is closed.'''
        raise NotImplementedError

    def request_new_data(self):
        '''Request new data from sensor.'''
        return

    def read_new_data(self):
        '''Try to read in new data from sensor. This must not take longer than max_read_new_data_period. Sensor must override.'''
        raise NotImplementedError

    def setup(self):
        '''Called before collection loop starts. Driver can override to make connection to sensor.'''
        return

    def pause(self):
        '''Called when pause command is received or sensor closes. Driver can override to notify sensor.'''
        return

    def resume(self):
        '''Called when resume command is received. Driver can override to notify sensor.'''
        return

    def handle_special_command(self, command, command_args):
        '''Override to handle sensor specified commands (e.g. trigger)'''
        return

    def driver_handle_new_setting(self, setting_name, setting_value):
        '''Override to allow certain settings to be changed as driver is open.'''
        return

    def send_status_update(self):
        '''
        Notify controller of status change (status = state + health + paused)
        This is called automatically when class fields change.
        '''
        self._send_message('new_sensor_status', (self.state, self.health, self.paused))

    def should_have_new_reading(self):
        '''Return true if enough time has elapsed that the sensor should have returned a new reading.'''
        time_since_last_data = self.sys_time - self.last_received_data_time
        # Increase read period a little bit since some sensors aren't 100% consistent in their
        # output rate. Don't want to report time-out if only a fraction late reading data.
        return time_since_last_data >= (self.desired_read_period * 1.2)

    def should_record_data(self):
        '''Return true if the sensor is in a state where it should be trying to record data.'''
        still_need_time_reference = self.wait_for_valid_time and self.utc_time == 0
        return not (still_need_time_reference or self.paused)

    def send_text(self, text):
        '''Send text message to controller (like print)'''
        self._send_message('new_sensor_text', text)

    def send_event(self, event_name, event_args=None):
        '''Send event to notify controller something important happened.'''
        self._send_message('new_sensor_event', (event_name, event_args))

    def _send_message(self, message_type, message_body):
        '''Send message to controller.'''
        self.controller_connection.send_message(message_type, message_body)

    def handle_data(self, utc_time, sys_time, data, data_ok=True):
        '''Send data to controller.  If data_ok is false then that indicates the data shouldn't be trusted or logged.'''
        self.last_received_data_time = self.sys_time
        # Make sure data is sent as a tuple.
        self._send_message('new_sensor_data', (utc_time, sys_time, data, data_ok))
        self.num_data_messages_sent += 1

    def handle_command(self, connection, command_name, command_args):
        '''
        Deal with a new command (e.g. 'close') received from controller.

        If the command isn't a generic one then it will be passed to handle_special_command.
        '''
        if command_name == 'close':
            self.received_close_request = True
        elif command_name == 'pause':
            self.paused = True
            self.pause()
        elif command_name == 'resume':
            self.paused = False
            self.resume()
        else:
            self.handle_special_command(command_name, command_args)

    def handle_new_time(self, connection, new_utc_time, new_sys_time):
        '''
        Process new time reference received from controller.

        Correct for any time that has elapsed since utc_time was last updated.
        Save this time off so we can use it to calculate a more precise timestamp later.
        '''
        self._last_received_sys_time = self.sys_time
        corrected_utc_time = new_utc_time + (self._last_received_sys_time - new_sys_time)
        self._last_received_utc_time = corrected_utc_time

    def handle_change_setting(self, connection, setting_name, setting_value):

        # All drivers need to support setting a data file directory so handle that here in base class.
        if setting_name == 'data_file_directory':
            self.override_data_file_directory = setting_value

        # Allow driver a chance to deal with setting.
        self.driver_handle_new_setting(setting_name, setting_value)

    def _need_to_run_processing_loop(self):
        '''Return true if it's time to run interface processing loop.'''
        return self.sys_time >= self.next_processing_loop_start_time

    def _need_to_run_sensor_loop(self):
        '''Return true if it's time to run sensor processing loop.'''
        enough_time_elapsed = self.sys_time >= self.next_sensor_loop_start_time

        return enough_time_elapsed or (not self.throttle_sensor_read) or self.still_waiting_for_data
