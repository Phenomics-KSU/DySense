# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensor_view_widget_designer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_sensor_view(object):
    def setupUi(self, sensor_view):
        sensor_view.setObjectName(_fromUtf8("sensor_view"))
        sensor_view.resize(677, 422)
        self.verticalLayout = QtGui.QVBoxLayout(sensor_view)
        self.verticalLayout.setMargin(6)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.top_horizontal_layout = QtGui.QHBoxLayout()
        self.top_horizontal_layout.setObjectName(_fromUtf8("top_horizontal_layout"))
        self.sensor_status_group_box = QtGui.QGroupBox(sensor_view)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sensor_status_group_box.setFont(font)
        self.sensor_status_group_box.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_status_group_box.setObjectName(_fromUtf8("sensor_status_group_box"))
        self.gridLayout_3 = QtGui.QGridLayout(self.sensor_status_group_box)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.sensor_health_label = QtGui.QLabel(self.sensor_status_group_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_health_label.sizePolicy().hasHeightForWidth())
        self.sensor_health_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensor_health_label.setFont(font)
        self.sensor_health_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_health_label.setObjectName(_fromUtf8("sensor_health_label"))
        self.gridLayout_3.addWidget(self.sensor_health_label, 0, 0, 1, 1)
        self.sensor_state_label = QtGui.QLabel(self.sensor_status_group_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_state_label.sizePolicy().hasHeightForWidth())
        self.sensor_state_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensor_state_label.setFont(font)
        self.sensor_state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_state_label.setObjectName(_fromUtf8("sensor_state_label"))
        self.gridLayout_3.addWidget(self.sensor_state_label, 1, 0, 1, 1)
        self.sensor_state_value_label = QtGui.QLabel(self.sensor_status_group_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_state_value_label.sizePolicy().hasHeightForWidth())
        self.sensor_state_value_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensor_state_value_label.setFont(font)
        self.sensor_state_value_label.setObjectName(_fromUtf8("sensor_state_value_label"))
        self.gridLayout_3.addWidget(self.sensor_state_value_label, 1, 1, 1, 1)
        self.paused_label = QtGui.QLabel(self.sensor_status_group_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paused_label.sizePolicy().hasHeightForWidth())
        self.paused_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paused_label.setFont(font)
        self.paused_label.setObjectName(_fromUtf8("paused_label"))
        self.gridLayout_3.addWidget(self.paused_label, 2, 1, 1, 1)
        self.sensor_paused_label = QtGui.QLabel(self.sensor_status_group_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_paused_label.sizePolicy().hasHeightForWidth())
        self.sensor_paused_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensor_paused_label.setFont(font)
        self.sensor_paused_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sensor_paused_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_paused_label.setObjectName(_fromUtf8("sensor_paused_label"))
        self.gridLayout_3.addWidget(self.sensor_paused_label, 2, 0, 1, 1)
        self.sensor_health_value_label = QtGui.QLabel(self.sensor_status_group_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_health_value_label.sizePolicy().hasHeightForWidth())
        self.sensor_health_value_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensor_health_value_label.setFont(font)
        self.sensor_health_value_label.setObjectName(_fromUtf8("sensor_health_value_label"))
        self.gridLayout_3.addWidget(self.sensor_health_value_label, 0, 1, 1, 1)
        self.top_horizontal_layout.addWidget(self.sensor_status_group_box)
        self.sensor_info_group_box = QtGui.QGroupBox(sensor_view)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sensor_info_group_box.setFont(font)
        self.sensor_info_group_box.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_info_group_box.setObjectName(_fromUtf8("sensor_info_group_box"))
        self.gridLayout_2 = QtGui.QGridLayout(self.sensor_info_group_box)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sensor_name_line_edit = QtGui.QLineEdit(self.sensor_info_group_box)
        self.sensor_name_line_edit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_name_line_edit.sizePolicy().hasHeightForWidth())
        self.sensor_name_line_edit.setSizePolicy(sizePolicy)
        self.sensor_name_line_edit.setObjectName(_fromUtf8("sensor_name_line_edit"))
        self.gridLayout_2.addWidget(self.sensor_name_line_edit, 1, 1, 1, 1)
        self.sensor_type_line_edit = QtGui.QLineEdit(self.sensor_info_group_box)
        self.sensor_type_line_edit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_type_line_edit.sizePolicy().hasHeightForWidth())
        self.sensor_type_line_edit.setSizePolicy(sizePolicy)
        self.sensor_type_line_edit.setReadOnly(False)
        self.sensor_type_line_edit.setObjectName(_fromUtf8("sensor_type_line_edit"))
        self.gridLayout_2.addWidget(self.sensor_type_line_edit, 2, 1, 1, 1)
        self.sensor_name_label = QtGui.QLabel(self.sensor_info_group_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensor_name_label.setFont(font)
        self.sensor_name_label.setObjectName(_fromUtf8("sensor_name_label"))
        self.gridLayout_2.addWidget(self.sensor_name_label, 1, 0, 1, 1)
        self.sensor_type_label = QtGui.QLabel(self.sensor_info_group_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_type_label.sizePolicy().hasHeightForWidth())
        self.sensor_type_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensor_type_label.setFont(font)
        self.sensor_type_label.setObjectName(_fromUtf8("sensor_type_label"))
        self.gridLayout_2.addWidget(self.sensor_type_label, 2, 0, 1, 1)
        self.sensor_id_label = QtGui.QLabel(self.sensor_info_group_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensor_id_label.setFont(font)
        self.sensor_id_label.setToolTip(_fromUtf8(""))
        self.sensor_id_label.setObjectName(_fromUtf8("sensor_id_label"))
        self.gridLayout_2.addWidget(self.sensor_id_label, 4, 0, 1, 1)
        self.sensor_id_line_edit = QtGui.QLineEdit(self.sensor_info_group_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_id_line_edit.sizePolicy().hasHeightForWidth())
        self.sensor_id_line_edit.setSizePolicy(sizePolicy)
        self.sensor_id_line_edit.setObjectName(_fromUtf8("sensor_id_line_edit"))
        self.gridLayout_2.addWidget(self.sensor_id_line_edit, 4, 1, 1, 1)
        self.top_horizontal_layout.addWidget(self.sensor_info_group_box)
        self.verticalLayout.addLayout(self.top_horizontal_layout)
        spacerItem = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.position_group_box = QtGui.QGroupBox(sensor_view)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.position_group_box.setFont(font)
        self.position_group_box.setAlignment(QtCore.Qt.AlignCenter)
        self.position_group_box.setObjectName(_fromUtf8("position_group_box"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.position_group_box)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.forward_position_label = QtGui.QLabel(self.position_group_box)
        self.forward_position_label.setObjectName(_fromUtf8("forward_position_label"))
        self.horizontalLayout_4.addWidget(self.forward_position_label)
        self.forward_position_line_edit = QtGui.QLineEdit(self.position_group_box)
        self.forward_position_line_edit.setText(_fromUtf8(""))
        self.forward_position_line_edit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.forward_position_line_edit.setObjectName(_fromUtf8("forward_position_line_edit"))
        self.horizontalLayout_4.addWidget(self.forward_position_line_edit)
        self.right_position_label = QtGui.QLabel(self.position_group_box)
        self.right_position_label.setObjectName(_fromUtf8("right_position_label"))
        self.horizontalLayout_4.addWidget(self.right_position_label)
        self.right_position_line_edit = QtGui.QLineEdit(self.position_group_box)
        self.right_position_line_edit.setObjectName(_fromUtf8("right_position_line_edit"))
        self.horizontalLayout_4.addWidget(self.right_position_line_edit)
        self.down_position_label = QtGui.QLabel(self.position_group_box)
        self.down_position_label.setObjectName(_fromUtf8("down_position_label"))
        self.horizontalLayout_4.addWidget(self.down_position_label)
        self.down_position_line_edit = QtGui.QLineEdit(self.position_group_box)
        self.down_position_line_edit.setObjectName(_fromUtf8("down_position_line_edit"))
        self.horizontalLayout_4.addWidget(self.down_position_line_edit)
        self.horizontalLayout_3.addWidget(self.position_group_box)
        self.orientation_group_box = QtGui.QGroupBox(sensor_view)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.orientation_group_box.setFont(font)
        self.orientation_group_box.setAlignment(QtCore.Qt.AlignCenter)
        self.orientation_group_box.setObjectName(_fromUtf8("orientation_group_box"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.orientation_group_box)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.roll_orientation_label = QtGui.QLabel(self.orientation_group_box)
        self.roll_orientation_label.setObjectName(_fromUtf8("roll_orientation_label"))
        self.horizontalLayout_5.addWidget(self.roll_orientation_label)
        self.roll_orientation_line_edit = QtGui.QLineEdit(self.orientation_group_box)
        self.roll_orientation_line_edit.setObjectName(_fromUtf8("roll_orientation_line_edit"))
        self.horizontalLayout_5.addWidget(self.roll_orientation_line_edit)
        self.pitch_orientation_label = QtGui.QLabel(self.orientation_group_box)
        self.pitch_orientation_label.setObjectName(_fromUtf8("pitch_orientation_label"))
        self.horizontalLayout_5.addWidget(self.pitch_orientation_label)
        self.pitch_orientation_line_edit = QtGui.QLineEdit(self.orientation_group_box)
        self.pitch_orientation_line_edit.setObjectName(_fromUtf8("pitch_orientation_line_edit"))
        self.horizontalLayout_5.addWidget(self.pitch_orientation_line_edit)
        self.yaw_orientation_label = QtGui.QLabel(self.orientation_group_box)
        self.yaw_orientation_label.setObjectName(_fromUtf8("yaw_orientation_label"))
        self.horizontalLayout_5.addWidget(self.yaw_orientation_label)
        self.yaw_orientation_line_edit = QtGui.QLineEdit(self.orientation_group_box)
        self.yaw_orientation_line_edit.setObjectName(_fromUtf8("yaw_orientation_line_edit"))
        self.horizontalLayout_5.addWidget(self.yaw_orientation_line_edit)
        self.horizontalLayout_3.addWidget(self.orientation_group_box)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.message_center_label = QtGui.QLabel(sensor_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_center_label.sizePolicy().hasHeightForWidth())
        self.message_center_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.message_center_label.setFont(font)
        self.message_center_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.message_center_label.setObjectName(_fromUtf8("message_center_label"))
        self.verticalLayout_3.addWidget(self.message_center_label)
        self.sensor_message_center_text_edit = QtGui.QTextEdit(sensor_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_message_center_text_edit.sizePolicy().hasHeightForWidth())
        self.sensor_message_center_text_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sensor_message_center_text_edit.setFont(font)
        self.sensor_message_center_text_edit.setObjectName(_fromUtf8("sensor_message_center_text_edit"))
        self.verticalLayout_3.addWidget(self.sensor_message_center_text_edit)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.data_group_box = QtGui.QGroupBox(sensor_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_group_box.sizePolicy().hasHeightForWidth())
        self.data_group_box.setSizePolicy(sizePolicy)
        self.data_group_box.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.data_group_box.setFont(font)
        self.data_group_box.setAlignment(QtCore.Qt.AlignCenter)
        self.data_group_box.setObjectName(_fromUtf8("data_group_box"))
        self.verticalLayout.addWidget(self.data_group_box)
        self.commands_group_box = QtGui.QGroupBox(sensor_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commands_group_box.sizePolicy().hasHeightForWidth())
        self.commands_group_box.setSizePolicy(sizePolicy)
        self.commands_group_box.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.commands_group_box.setFont(font)
        self.commands_group_box.setAlignment(QtCore.Qt.AlignCenter)
        self.commands_group_box.setObjectName(_fromUtf8("commands_group_box"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.commands_group_box)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.setup_sensor_button = QtGui.QPushButton(self.commands_group_box)
        self.setup_sensor_button.setMinimumSize(QtCore.QSize(0, 30))
        self.setup_sensor_button.setObjectName(_fromUtf8("setup_sensor_button"))
        self.horizontalLayout_6.addWidget(self.setup_sensor_button)
        self.start_sensor_button = QtGui.QPushButton(self.commands_group_box)
        self.start_sensor_button.setMinimumSize(QtCore.QSize(0, 30))
        self.start_sensor_button.setObjectName(_fromUtf8("start_sensor_button"))
        self.horizontalLayout_6.addWidget(self.start_sensor_button)
        self.pause_sensor_button = QtGui.QPushButton(self.commands_group_box)
        self.pause_sensor_button.setMinimumSize(QtCore.QSize(0, 30))
        self.pause_sensor_button.setObjectName(_fromUtf8("pause_sensor_button"))
        self.horizontalLayout_6.addWidget(self.pause_sensor_button)
        self.close_sensor_button = QtGui.QPushButton(self.commands_group_box)
        self.close_sensor_button.setMinimumSize(QtCore.QSize(0, 30))
        self.close_sensor_button.setObjectName(_fromUtf8("close_sensor_button"))
        self.horizontalLayout_6.addWidget(self.close_sensor_button)
        self.remove_sensor_button = QtGui.QPushButton(self.commands_group_box)
        self.remove_sensor_button.setMinimumSize(QtCore.QSize(0, 30))
        self.remove_sensor_button.setObjectName(_fromUtf8("remove_sensor_button"))
        self.horizontalLayout_6.addWidget(self.remove_sensor_button)
        self.verticalLayout.addWidget(self.commands_group_box)
        self.special_commands_group_box = QtGui.QGroupBox(sensor_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.special_commands_group_box.sizePolicy().hasHeightForWidth())
        self.special_commands_group_box.setSizePolicy(sizePolicy)
        self.special_commands_group_box.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.special_commands_group_box.setFont(font)
        self.special_commands_group_box.setAlignment(QtCore.Qt.AlignCenter)
        self.special_commands_group_box.setObjectName(_fromUtf8("special_commands_group_box"))
        self.verticalLayout.addWidget(self.special_commands_group_box)
        self.special_commands_group_box.raise_()
        self.commands_group_box.raise_()
        self.data_group_box.raise_()

        self.retranslateUi(sensor_view)
        QtCore.QMetaObject.connectSlotsByName(sensor_view)
        sensor_view.setTabOrder(self.sensor_name_line_edit, self.sensor_type_line_edit)
        sensor_view.setTabOrder(self.sensor_type_line_edit, self.sensor_id_line_edit)
        sensor_view.setTabOrder(self.sensor_id_line_edit, self.forward_position_line_edit)
        sensor_view.setTabOrder(self.forward_position_line_edit, self.right_position_line_edit)
        sensor_view.setTabOrder(self.right_position_line_edit, self.down_position_line_edit)
        sensor_view.setTabOrder(self.down_position_line_edit, self.roll_orientation_line_edit)
        sensor_view.setTabOrder(self.roll_orientation_line_edit, self.pitch_orientation_line_edit)
        sensor_view.setTabOrder(self.pitch_orientation_line_edit, self.yaw_orientation_line_edit)
        sensor_view.setTabOrder(self.yaw_orientation_line_edit, self.sensor_message_center_text_edit)
        sensor_view.setTabOrder(self.sensor_message_center_text_edit, self.setup_sensor_button)
        sensor_view.setTabOrder(self.setup_sensor_button, self.start_sensor_button)
        sensor_view.setTabOrder(self.start_sensor_button, self.pause_sensor_button)
        sensor_view.setTabOrder(self.pause_sensor_button, self.close_sensor_button)
        sensor_view.setTabOrder(self.close_sensor_button, self.remove_sensor_button)

    def retranslateUi(self, sensor_view):
        sensor_view.setWindowTitle(_translate("sensor_view", "Form", None))
        self.sensor_status_group_box.setTitle(_translate("sensor_view", "Current Status", None))
        self.sensor_health_label.setText(_translate("sensor_view", " Health:", None))
        self.sensor_state_label.setText(_translate("sensor_view", "State:", None))
        self.sensor_state_value_label.setText(_translate("sensor_view", "Unknown", None))
        self.paused_label.setText(_translate("sensor_view", "Paused", None))
        self.sensor_paused_label.setText(_translate("sensor_view", "Saving:", None))
        self.sensor_health_value_label.setText(_translate("sensor_view", "N/A", None))
        self.sensor_info_group_box.setTitle(_translate("sensor_view", "Common Settings", None))
        self.sensor_name_label.setText(_translate("sensor_view", "Name", None))
        self.sensor_type_label.setText(_translate("sensor_view", "Type", None))
        self.sensor_id_label.setText(_translate("sensor_view", "Tag", None))
        self.position_group_box.setTitle(_translate("sensor_view", "Position Offsets (meters)", None))
        self.forward_position_label.setText(_translate("sensor_view", "Forward:", None))
        self.right_position_label.setText(_translate("sensor_view", "Right:", None))
        self.down_position_label.setText(_translate("sensor_view", "Down:", None))
        self.orientation_group_box.setTitle(_translate("sensor_view", "Orientation Offsets (degrees)", None))
        self.roll_orientation_label.setText(_translate("sensor_view", "Roll:", None))
        self.pitch_orientation_label.setText(_translate("sensor_view", "Pitch:", None))
        self.yaw_orientation_label.setText(_translate("sensor_view", "Yaw:", None))
        self.message_center_label.setText(_translate("sensor_view", "Message Center", None))
        self.data_group_box.setTitle(_translate("sensor_view", "Data", None))
        self.commands_group_box.setTitle(_translate("sensor_view", "Commands", None))
        self.setup_sensor_button.setText(_translate("sensor_view", "Setup", None))
        self.start_sensor_button.setText(_translate("sensor_view", "Start", None))
        self.pause_sensor_button.setText(_translate("sensor_view", "Pause", None))
        self.close_sensor_button.setText(_translate("sensor_view", "Close", None))
        self.remove_sensor_button.setText(_translate("sensor_view", "Remove", None))
        self.special_commands_group_box.setTitle(_translate("sensor_view", "Special Commands", None))

