#!/usr/bin/env python

import time
import os
import logging
import sys
import threading
import subprocess
import json

class SensorCloseTimeout(Exception): pass

class SensorDriverFactory(object):
    
    def __init__(self, context, local_endpoint, remote_endpoint):
        self.context = context
        self.local_endpoint = local_endpoint
        self.remote_endpoint = remote_endpoint

    def create_sensor(self, sensor_type, sensor_id, sensor_settings):
        '''
        '''
        sensor = None
        
        local_startup_args = [sensor_id, sensor_settings, self.context, self.local_endpoint]
        remote_startup_args = [sensor_id, sensor_settings, self.remote_endpoint]
        
        # Use local imports for threads in case they have dependencies that other users don't care about.
        if sensor_type == 'greenseeker':
            from sensors.nvdi.greenseeker import GreenSeeker
            sensor = SensorDriverThread(GreenSeeker, local_startup_args)
        if sensor_type == 'irt_ue':
            from sensors.irt.irt_ue import IRT_UE
            sensor = SensorDriverThread(IRT_UE, local_startup_args)
        if sensor_type == 'test_sensor_python':
            from sensors.test.test_sensor_python import TestSensor
            sensor = SensorDriverThread(TestSensor, local_startup_args)
            #sensor = SensorDriverProcess('../sensors/test.py', remote_startup_args, language='python')
        if sensor_type == 'test_sensor_csharp':
            sensor = SensorDriverProcess('../sensors/test/test_sensor_csharp/DySenseTestSensorCS.exe', remote_startup_args, language='csharp')
        if sensor_type == 'kinectv2_msdk':
            sensor = SensorDriverProcess('../sensors/kinect/kinectv2_msdk/DySenseKinectV2.exe', remote_startup_args, language='csharp')
        if sensor_type == 'gps_nmea_test':
            from sensors.gps.gps_nmea_test import GpsNmeaTest
            sensor = SensorDriverThread(GpsNmeaTest, local_startup_args)
        
        sensor.run()
        
        return sensor
    
class SensorDriverThread(object):
    
    def __init__(self, driver_class, startup_args):
        
        self.driver_class = driver_class
        self.startup_args = startup_args
        self.sensor = None
        self.sensor_thread = None

    def run(self):
        
        self.sensor = self.driver_class(*self.startup_args)
        
        # We want it to be a daemon thread so it doesn't keep the process from closing.
        self.sensor_thread = threading.Thread(target=self.sensor.run)
        self.sensor_thread.setDaemon(True)
        self.sensor_thread.start()
    
    def close(self, timeout):
        
        if not self.sensor_thread:
            return # already closed
        
        try:
            self.sensor_thread.join(timeout)
            if self.sensor_thread.is_alive():
                raise SensorCloseTimeout()
        finally:
            self.sensor_thread = None
            self.sensor = None
    
class SensorDriverProcess(object):
    
    def __init__(self, relative_path, startup_args, language="N/A"):
        self.relative_path = relative_path
        self.startup_args = startup_args
        self.language = language.lower()
        self.thread = None
        self.process = None

    def run(self):
        
        # We want it to be a daemon thread so it doesn't keep the process from closing.
        self.thread = threading.Thread(target=self._run_process, args=[self.relative_path, self.startup_args, self.language])
        self.thread.setDaemon(True)
        self.thread.start()

    def _run_process(self, relative_path, startup_args, language):
        
        startup_args[0] = str(startup_args[0]) # make sure ID is a string.
        startup_args[1] = json.dumps(startup_args[1]) # serialize sensor settings
    
        absolute_path = os.path.join(os.path.abspath(sys.path[0]), relative_path)
        try:
            if language == 'python':
                # Need to include sys.executable when executing a python script.
                self.process = subprocess.Popen([sys.executable, absolute_path] + startup_args, shell=False)
            else: 
                # Run general process startup. 
                self.process = subprocess.Popen([absolute_path] + startup_args, shell=False)
        except WindowsError:
            print absolute_path
            raise
        
        self.process.wait()

    def close(self, timeout):
        
        if not self.thread:
            return # already closed
        
        self.thread.join(timeout)
        if self.thread.is_alive():
            if self.process:
                self.process.terminate()
            self.thread.join(timeout=2)
            if self.thread.is_alive():
                raise SensorCloseTimeout
        