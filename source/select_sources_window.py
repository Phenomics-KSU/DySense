#!/usr/bin/env python

import sys
from PyQt4.Qt import *
from PyQt4 import QtGui

class SelectSourcesWindow(QDialog):
    
    new_sources_selected = pyqtSignal(dict, list, list)
    
    def __init__(self, presenter, controller_info, sensors, *args):
        QDialog.__init__(self, *args)
        
        self.presenter = presenter
        
        # Used to associate sensor info with checkbox.
        self.checkbox_to_position_sensor = {}
        self.position_sensor_to_checkbox = {}
        
        # Used to associate combo box index with sensor info.
        self.possible_time_sensors = []
        
        self.setWindowTitle('Select Sources')
        self.setWindowIcon(QtGui.QIcon('../resources/dysense_logo_no_text.png'))
        self.setMinimumWidth(205)
        
        self.central_layout = QVBoxLayout(self)

        self.setup_time_box(controller_info, sensors)
        self.setup_orientation_box(controller_info, sensors)
        self.setup_position_box(controller_info, sensors)
        self.setup_buttons()
        
        self.central_layout.addWidget(self.time_group_box)
        self.central_layout.addWidget(self.position_group_box)
        self.central_layout.addWidget(self.orientation_group_box)
        self.central_layout.addLayout(self.button_layout)
        
    def setup_time_box(self, controller_info, sensors):
        
        self.time_group_box = QGroupBox("time")
        self.time_group_box.setTitle("Time")
        self.time_group_box.setAlignment(Qt.AlignHCenter)
        self.time_selector = QComboBox(self.time_group_box)
        self.time_gb_layout = QVBoxLayout()
        self.time_gb_layout.addWidget(self.time_selector)
        self.time_group_box.setLayout(self.time_gb_layout)
        
        self.possible_time_sensors = self.find_sensors_with_tag(sensors, 'time')
        possible_time_sensors_names = [s['sensor_name'] for s in self.possible_time_sensors]

        self.time_selector.addItems(possible_time_sensors_names)
        
        try:
            current_time_id = controller_info['time_source']['sensor_id']
            current_time_sensor = [s for s in self.possible_time_sensors if s['sensor_id'] == current_time_id][0]
            active_idx = self.possible_time_sensors.index(current_time_sensor['sensor_name'])
            self.time_selector.setCurrentIndex(active_idx)
        except (ValueError, IndexError, TypeError):
            pass
        
    def setup_orientation_box(self, controller_info, sensors):
        
        self.orientation_group_box = QGroupBox("orientation")
        self.orientation_group_box.setTitle("Orientation")
        self.orientation_group_box.setAlignment(Qt.AlignHCenter)
        
        self.roll_selector = QComboBox(self.orientation_group_box)
        self.roll_label = QLabel("Roll:")
        self.roll_label.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred))
        
        self.pitch_selector = QComboBox(self.orientation_group_box)
        self.pitch_label = QLabel("Pitch:")
        self.pitch_label.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred))
        
        self.yaw_selector = QComboBox(self.orientation_group_box)
        self.yaw_label = QLabel("Yaw:")
        self.yaw_label.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred))
        
        self.orientation_gb_layout = QGridLayout()
        self.orientation_gb_layout.addWidget(self.roll_label, 0, 1)
        self.orientation_gb_layout.addWidget(self.roll_selector, 0, 2)
        self.orientation_gb_layout.addWidget(self.pitch_label, 1, 1)
        self.orientation_gb_layout.addWidget(self.pitch_selector, 1, 2)
        self.orientation_gb_layout.addWidget(self.yaw_label, 2, 1)
        self.orientation_gb_layout.addWidget(self.yaw_selector, 2, 2)
        
        self.orientation_group_box.setLayout(self.orientation_gb_layout)
        
    def setup_position_box(self, controller_info, sensors):
        
        self.position_group_box = QGroupBox("position")
        self.position_group_box.setTitle("Position")
        self.position_group_box.setAlignment(Qt.AlignHCenter)
        
        self.position_gb_layout = QVBoxLayout()
        
        possible_position_sensors = self.find_sensors_with_tag(sensors, 'position')
        for sensor_info in possible_position_sensors:
            checkbox = QCheckBox()
            checkbox.setText(sensor_info['sensor_name'])
            
            self.position_sensor_to_checkbox[sensor_info['sensor_id']] = checkbox
            self.checkbox_to_position_sensor[checkbox] = sensor_info
            
            # TODO update for multiple controllers
            for current_position_source in controller_info['position_sources']:
                if current_position_source['sensor_id'] == sensor_info['sensor_id']:
                    checkbox.setChecked(True)
            
            self.position_gb_layout.addWidget(checkbox)
        
        self.position_group_box.setLayout(self.position_gb_layout)

    def setup_buttons(self):
        
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.ok_button_clicked)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addWidget(self.ok_button)

    def find_sensors_with_tag(self, sensors, tag):
        
        sensor_info_with_tag = []
        for sensor_info in sensors.values():
            metadata = sensor_info['metadata']
            if tag in [t.lower() for t in metadata.get('tags', [])]:
                sensor_info_with_tag.append(sensor_info)
        
        return sensor_info_with_tag
    
    def ok_button_clicked(self):
        
        try:
            time_source_info = self.possible_time_sensors[self.time_selector.currentIndex()]
        except IndexError:
            time_source_info = None
        
        position_sources = []
        for checkbox, sensor_info in self.checkbox_to_position_sensor.iteritems():
            if checkbox.isChecked():
                position_sources.append(sensor_info)
        
        orientation_sources = [] # TODO

        self.presenter.change_controller_info('time_source', time_source_info)
        self.presenter.change_controller_info('position_sources', position_sources)
        self.presenter.change_controller_info('orientation_sources', orientation_sources)
        
        self.close()
        
    def cancel_button_clicked(self):
        
        self.close()
        