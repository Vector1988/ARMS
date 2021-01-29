# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uimain.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import uilogin

class Ui_MainWindow(QWidget):

    main_show_signal = pyqtSignal()
    main_hide_signal = pyqtSignal()

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        #self.setObjectName("MainWindow")
        self.resize(1366, 768)
        self.setMinimumSize(QtCore.QSize(1366, 768))
        self.setMaximumSize(QtCore.QSize(1366, 768))
        self.alarm_show_Button = QtWidgets.QPushButton(self)
        self.alarm_show_Button.setGeometry(QtCore.QRect(170, 180, 411, 131))
        self.alarm_show_Button.setObjectName("alarm_show_Button")
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        #self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setNativeMenuBar(False)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "药品不良反应预警分析系统"))

    def setupUi(self, Form):
        self.test_signal.emit()
        Form1.resize(1024, 768)
        Form1.setMinimumSize(QtCore.QSize(800, 600))
        Form1.setMaximumSize(QtCore.QSize(800, 600))
        self.treeView = QtWidgets.QTreeView(Form1)
        self.treeView.setGeometry(QtCore.QRect(40, 90, 271, 401))
        self.treeView.setObjectName("treeView")
        self.checkButton = QtWidgets.QPushButton(Form1)
        self.checkButton.setGeometry(QtCore.QRect(490, 130, 75, 23))
        self.checkButton.setObjectName("checkButton")
        self.toolButton = QtWidgets.QToolButton(Form1)
        self.toolButton.setGeometry(QtCore.QRect(580, 130, 37, 18))
        self.toolButton.setObjectName("toolButton")
        self.radioButton = QtWidgets.QRadioButton(Form1)
        self.radioButton.setGeometry(QtCore.QRect(450, 180, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form1)
        self.radioButton_2.setGeometry(QtCore.QRect(580, 180, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")


    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_hide(self):
        self.test_signal.emit()
        self.hide()