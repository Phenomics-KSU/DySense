# Use default python types instead of QVariant
import sip
sip.setapi('QVariant', 2)

from PyQt4.QtGui import *
from sensor_view_widget_designer import Ui_Form
from PyQt4 import QtGui
import yaml




class SensorViewWidget(QWidget,Ui_Form):
           
    def __init__(self, controller_id, sensor_info, presenter):
        #super().__init__()
        QWidget.__init__(self)
        self.setupUi(self) #call the auto-generated setupUi function in the designer file
        
        self.presenter = presenter
        self.controller_id = controller_id
        self.sensor_info = sensor_info
        self.sensor_metadata = sensor_info['metadata']
        self.sensor_id = sensor_info['sensor_id']
        
        #dictionaries for relating the sensor info names to their corresponding line edits/labels        
        self.name_to_object =  {
                               'sensor_type': self.sensor_type_line_edit,
                               'sensor_name': self.sensor_name_line_edit,                                      
                               'sensor_state': self.sensor_state_value_label,
                               
                               'instrument_id': self.sensor_id_line_edit,
                               'position_offsets': [self.forward_position_line_edit,
                                                    self.left_position_line_edit,
                                                    self.up_position_line_edit],
                               'orientation_offsets': [self.roll_orientation_line_edit,
                                                       self.pitch_orientation_line_edit,
                                                       self.yaw_orientation_line_edit],          
                               }
        
        self.object_to_name =  {
                               self.sensor_id_line_edit: 'instrument_id', 
                               self.sensor_type_line_edit: 'sensor_type',
                               self.sensor_name_line_edit: 'sensor_name',                                      
                               self.sensor_state_value_label: 'sensor_state',
                               self.forward_position_line_edit: 'position_offsets',
                               self.left_position_line_edit: 'position_offsets',
                               self.up_position_line_edit: 'position_offsets',
                               self.roll_orientation_line_edit: 'orientation_offsets',
                               self.pitch_orientation_line_edit: 'orientation_offsets',
                               self.yaw_orientation_line_edit: 'orientation_offsets',
                               }
             
        
        self.settings_name_to_object = {}
                                        #'output_rate': self.capture_rate_line_edit                                                                           
                                        
        
        
        
#         
#          new_gps_info['settings'] = {'test_file_path': "..nmea_logs\SXBlueGGA.txt",
#                                            'output_rate': 1,
#                                            'required_fix': 'none',
#                                            'required_precision': 0}
#         
       
        
        self.set_gps_info_button.clicked.connect(self.set_gps_info)
                                                       
        
        
        
        
        
        
        
        
        
        
        #get type dependent settings from metadata
        #default_settings = self.sensor_info['settings']
        sensor_type = sensor_info['sensor_type']
        self.setup_settings(self.sensor_info['settings'])
        
        #set the special commands from metadata
        special_commands_list = self.sensor_metadata.get('special_commands', None)
        self.setup_special_commands(special_commands_list)
        
        
        #setup health icons #TODO crop whitespace from edges of icons and figure out why good_icon pixmap is null
        self.neutral_icon = QtGui.QPixmap('../resources/grey_neutral_icon.png')
        self.neutral_icon = self.neutral_icon.scaled(65,63)      
        self.good_icon = QtGui.QPixmap('../resources/green_check_icon.jpg')
        #self.good_icon = QtGui.QPixmap('../resources/grey_neutral_icon.png')
        self.good_icon = self.good_icon.scaled(65,63)
        self.bad_icon = QtGui.QPixmap('../resources/red_x_icon.png')
        self.bad_icon = self.bad_icon.scaled(65,63)
        
        
        #Set fields not to be edited by user as read only
        self.sensor_message_center_text_edit.setReadOnly(True)
           
        
        #Connect User Changes        
        #self.sensor_name_line_edit.textEdited.connect(self.sensor_name_changed)
        self.sensor_name_line_edit.editingFinished.connect(self.sensor_name_changed)
        self.sensor_id_line_edit.editingFinished.connect(self.instrument_id_changed)
        self.forward_position_line_edit.editingFinished.connect(self.position_offset_changed)
        self.left_position_line_edit.editingFinished.connect(self.position_offset_changed)
        self.up_position_line_edit.editingFinished.connect(self.position_offset_changed)
        self.roll_orientation_line_edit.editingFinished.connect(self.orientation_offset_changed)
        self.pitch_orientation_line_edit.editingFinished.connect(self.orientation_offset_changed)
        self.yaw_orientation_line_edit.editingFinished.connect(self.orientation_offset_changed)
                      
        #Connect main command buttons
        self.connect_sensor_button.clicked.connect(self.connect_sensor_button_clicked)
        self.pause_sensor_button.clicked.connect(self.pause_sensor_button_clicked)
        self.remove_sensor_button.clicked.connect(self.remove_sensor_button_clicked)
        
        #Connect clear button
        self.clear_sensor_message_center_button.clicked.connect(self.clear_sensor_message_center_button_clicked)
    
    # FOR TESTING
    def set_gps_info(self):
        
        if self.sensor_info['sensor_type'] != 'gps_nmea_test':
            return
         
        for key in self.setting_line_edit_references:
            if self.setting_line_edit_references[key] == 'test_file_path':
                key.setText(r"..\nmea_logs\SXBlueGGA.txt")
            
            elif self.setting_line_edit_references[key] == 'output_rate':
                key.setText('1')    
            
            elif self.setting_line_edit_references[key] == 'required_precision':
                key.setText('0')
                
            elif self.setting_line_edit_references[key] == 'required_fix':
                key.setText('none')
    def setup_settings(self, settings):
       
        self.settings_group_box_layout = QtGui.QGridLayout()
        self.settings_group_box.setLayout(self.settings_group_box_layout)
           
        # setting dictionary
        # key = line edit references
        # value = setting name
        self.setting_line_edit_references = {}
        
        # create dicts of the settings name labels, line edits, and units labels
        for n, setting_metadata in enumerate(self.sensor_metadata['settings']):    
            
            name = setting_metadata.get('name', 'No name in metadata')
            default_value = setting_metadata.get('default_value', 'no default')
            units = setting_metadata.get('units', '')
            
            self.name_label = QtGui.QLabel()
            self.units_label = QtGui.QLabel()
            self.line_edit = QtGui.QLineEdit()
            
            # Store the line edit references and corresponding name
            obj_ref = self.line_edit
            self.setting_line_edit_references[obj_ref] = name
            
            self.settings_group_box_layout.addWidget(self.name_label, n, 0)
            self.settings_group_box_layout.addWidget(self.line_edit, n, 1)
            self.settings_group_box_layout.addWidget(self.units_label, n, 2)
            
            self.name_label.setText(name.replace('_', ' ').title())   
            self.line_edit.setText(str(settings[name]))
            self.units_label.setText(units.replace('_', ' ').title())
            
            # Connect the line edit signal
            self.line_edit.editingFinished.connect(self.setting_changed_by_user)

        print self.setting_line_edit_references
        
    def setup_special_commands(self, special_commands):
        
        if special_commands == None:
            self.special_commands_group_box.deleteLater()
            return
        
        
        #special commands dict
        #key = reference
        #value = special command
        self.special_commands_references = {}
        
        special_commands_layout = QtGui.QHBoxLayout()
        self.special_commands_group_box.setLayout(special_commands_layout)
        for command in special_commands:
            
            b = QtGui.QPushButton(command.replace('_', ' ').title())
            special_commands_layout.addWidget(b)
            
            # store the button object reference 
            obj_ref = str(b).split()[3]
            self.special_commands_references[obj_ref] = command  
            
            b.clicked.connect(self.special_command_clicked)
                  
    def special_command_clicked(self):
                
        obj_ref = str(self.sender()).split()[3]    
        command = self.special_commands_references[obj_ref]
        
        self.presenter.send_sensor_command(command)       
        
    def setting_changed_by_user(self):
        new_value = str(self.sender().text())
        
        obj_ref = self.sender()  
        setting_name = self.setting_line_edit_references[obj_ref]
        print setting_name
        print new_value
        
        self.presenter.change_sensor_setting(setting_name, new_value)
            
    #Update Viewer
    def update_sensor_view(self, info_name, value):       
          
        # Update all screen objects that correspond to the specified sensor info name. 
        matching_obj = self.name_to_object.get(info_name, [])
        if not isinstance(matching_obj, list):
            matching_obj.setText(str(value))
        else:
            for i, obj in enumerate(matching_obj):
                obj.setText(str(value[i]))
        
        #get values from settings dict    
        if info_name == 'settings':
            settings = value
            #TODO correct how settings are updated - should be able to get rid of this now
            for key in settings:
                if isinstance(key,dict):
                    continue
                if self.settings_name_to_object.has_key(key):
                    obj = self.settings_name_to_object[key]
                    obj.setText(str(settings[key]))
                   
        if info_name == 'sensor_health':
            self.sensor_health_update(value)                        
            
        if info_name == 'sensor_paused':
            if value == True:
                self.paused_label.setText('Paused')
            elif value == False:
                self.paused_label.setText('Running')
    
    def sensor_name_changed(self):    
        
        new_name = str(self.sensor_name_line_edit.text())
        self.presenter.change_sensor_info('sensor_name', new_name)
        
    def instrument_id_changed(self):    
        
        new_value = str(self.sensor_id_line_edit.text())
        self.presenter.change_sensor_info('instrument_id', new_value)
         
    def position_offset_changed(self):    
        
        forward = str(self.forward_position_line_edit.text())
        left = str(self.left_position_line_edit.text())
        up = str(self.up_position_line_edit.text())
        self.presenter.change_sensor_info('position_offsets', [forward, left, up])     
     
    def orientation_offset_changed(self):    
        
        roll = str(self.roll_orientation_line_edit.text())
        pitch = str(self.pitch_orientation_line_edit.text())
        yaw = str(self.yaw_orientation_line_edit.text())
        self.presenter.change_sensor_info('orientation_offsets', [roll, pitch, yaw])        
    
    def sensor_health_update(self, health):
        if health == 'N/A' or 'neutral':
            self.sensor_health_icon_label.setPixmap(self.neutral_icon)    
    
        elif health == 'good':
            self.sensor_health_icon_label.setPixmap(self.good_icon)
            
        elif health == 'bad':
            self.sensor_health_icon_label.setPixmap(self.bad_icon)
    
        
    def clear_sensor_message_center_button_clicked(self):
        self.sensor_message_center_text_edit.clear() 
    
    
    #Main Commands
    def connect_sensor_button_clicked(self):
        print 'connect sensor button clicked'
        
    def pause_sensor_button_clicked(self):
        print 'pause sensor button clicked'
        
    def remove_sensor_button_clicked(self):    
        self.presenter.remove_sensor(self.sensor_id)    
        print 'remove sensor button clicked'
        
        
#     def extra_command1_button_clicked(self):
#         self.sensor_message_center_text_edit.setText(str(self.sensor_info['metadata']))
#         
#         print 'extra command 1 clicked'
#         
#     def extra_command2_button_clicked(self):
#         print'extra command 2 clicked'
            