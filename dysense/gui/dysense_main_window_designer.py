# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dysense_main_window_designer.ui'
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

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.setEnabled(True)
        main_window.resize(853, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        main_window.setFont(font)
        main_window.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.top_horizontal_layout = QtGui.QHBoxLayout()
        self.top_horizontal_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.top_horizontal_layout.setContentsMargins(-1, -1, -1, 0)
        self.top_horizontal_layout.setSpacing(3)
        self.top_horizontal_layout.setObjectName(_fromUtf8("top_horizontal_layout"))
        self.logo_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMinimumSize(QtCore.QSize(140, 40))
        self.logo_label.setMaximumSize(QtCore.QSize(140, 40))
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setObjectName(_fromUtf8("logo_label"))
        self.top_horizontal_layout.addWidget(self.logo_label)
        self.title_horizontal_layout = QtGui.QHBoxLayout()
        self.title_horizontal_layout.setSpacing(3)
        self.title_horizontal_layout.setObjectName(_fromUtf8("title_horizontal_layout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.title_horizontal_layout.addItem(spacerItem)
        self.menu_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy)
        self.menu_button.setMinimumSize(QtCore.QSize(240, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.menu_button.setFont(font)
        self.menu_button.setObjectName(_fromUtf8("menu_button"))
        self.title_horizontal_layout.addWidget(self.menu_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.title_horizontal_layout.addItem(spacerItem1)
        self.extras_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extras_button.sizePolicy().hasHeightForWidth())
        self.extras_button.setSizePolicy(sizePolicy)
        self.extras_button.setMinimumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.extras_button.setFont(font)
        self.extras_button.setObjectName(_fromUtf8("extras_button"))
        self.title_horizontal_layout.addWidget(self.extras_button)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.title_horizontal_layout.addItem(spacerItem2)
        self.top_horizontal_layout.addLayout(self.title_horizontal_layout)
        spacerItem3 = QtGui.QSpacerItem(140, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.top_horizontal_layout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.top_horizontal_layout)
        self.line = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.bottom_horizontal_layout = QtGui.QHBoxLayout()
        self.bottom_horizontal_layout.setObjectName(_fromUtf8("bottom_horizontal_layout"))
        self.sensor_list_widget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_list_widget.sizePolicy().hasHeightForWidth())
        self.sensor_list_widget.setSizePolicy(sizePolicy)
        self.sensor_list_widget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sensor_list_widget.setFont(font)
        self.sensor_list_widget.setObjectName(_fromUtf8("sensor_list_widget"))
        self.bottom_horizontal_layout.addWidget(self.sensor_list_widget)
        self.stacked_widget = QtGui.QStackedWidget(self.centralwidget)
        self.stacked_widget.setMinimumSize(QtCore.QSize(100, 0))
        self.stacked_widget.setObjectName(_fromUtf8("stacked_widget"))
        self.menu_page = QtGui.QWidget()
        self.menu_page.setObjectName(_fromUtf8("menu_page"))
        self.gridLayout_3 = QtGui.QGridLayout(self.menu_page)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.message_center_label = QtGui.QLabel(self.menu_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_center_label.sizePolicy().hasHeightForWidth())
        self.message_center_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.message_center_label.setFont(font)
        self.message_center_label.setAlignment(QtCore.Qt.AlignCenter)
        self.message_center_label.setObjectName(_fromUtf8("message_center_label"))
        self.gridLayout_3.addWidget(self.message_center_label, 2, 1, 1, 1)
        self.stacked_widget.addWidget(self.menu_page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stacked_widget.addWidget(self.page_2)
        self.bottom_horizontal_layout.addWidget(self.stacked_widget)
        self.verticalLayout.addLayout(self.bottom_horizontal_layout)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "MainWindow", None))
        self.logo_label.setText(_translate("main_window", "logo", None))
        self.menu_button.setText(_translate("main_window", "Main Menu", None))
        self.extras_button.setText(_translate("main_window", "Extras", None))
        self.message_center_label.setText(_translate("main_window", "Loading Controller...", None))
