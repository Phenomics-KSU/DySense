# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
from datetime import datetime
import calendar as cal

from gps_nmea import GpsNmea
from source.utility import make_unicode

class GpsNmeaTest(GpsNmea):

    def __init__(self, sensor_id, instrument_id, settings, context, connect_endpoint):
        
        try:
            self.test_file_path = make_unicode(settings['test_file_path'])
            self.output_rate = make_unicode(settings['output_rate'])
            self.required_fix = make_unicode(settings['required_fix'])
            self.required_latlon_error = float(settings['required_error'])
            self.min_sats = int(settings['min_sats'])
            self.output_rate = float(settings['output_rate'])
            self.output_period = 1.0 / self.output_rate
        except (KeyError, ValueError, ZeroDivisionError) as e:
            raise ValueError("Bad sensor setting.  Exception {}".format(repr(e)))
        
        GpsNmea.__init__(self, self.required_fix, self.required_latlon_error, self.min_sats,
                         sensor_id=sensor_id, instrument_id=instrument_id,
                         context=context, connect_endpoint=connect_endpoint)
        
        self.desired_read_period = self.output_period
        
        self.test_file = None
        
        # Set to true to run image latency tests instead of reading from file.
        self.latency_test = False
        self.latency_test_period = 0.001
        self.latency_test_start_utc = 0
        self.latency_mode_run_count = 0
        
    def is_closed(self):
        '''Return true if test file is closed.'''
        return self.closed
    
    def close(self):
        '''Set flag to signify that sensor is closed.'''
        self.closed = True
        
    def setup(self):
        
        if not os.path.isfile(self.test_file_path):
            raise Exception('The test file could not be found:\n\'{}\'\n'.format(self.test_file_path))
        else:
            self.test_file = open(self.test_file_path, 'r')
        
    def read_new_data(self):
        '''Read in new message from test file. Only called when not paused.'''
        
        if self.latency_test:
            self.latency_mode_run_count += 1
            current_time = self.sys_time - self.latency_test_start_time
            print current_time
            sys.stdout.flush()
            # Provide time source at a lower rate.
            if self.latency_mode_run_count % 50 == 0:
                self.handle_data(current_time, self.sys_time, [0, 0, 0, 0, 0])
            return 'normal'
        
        nmea_string = self.test_file.readline().strip()
        
        # For the very first message use the current system time for UTC time instead of what's
        # in the file because if the same test file is repeatedly used then directories that use
        # the starting UTC time will all be the same.
        if self.num_data_messages_sent == 0:
            utc_override = cal.timegm(datetime.timetuple(datetime.utcnow()))
        else:
            utc_override = None
        
        current_state = self.process_nmea_message(nmea_string, self.sys_time, utc_override)
        
        return current_state

    def handle_special_command(self, command):
            
        if command == 'latency_test':
            self.latency_test = not self.latency_test
            if self.latency_test:
                self.latency_test_start_time = self.sys_time
                self.desired_read_period = self.latency_test_period
            else:
                # Restore original reading rate.
                self.desired_read_period = self.output_period
