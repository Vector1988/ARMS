# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test-form1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.setWindowModality(QtCore.Qt.ApplicationModal)
        Form1.resize(1366, 768)
        Form1.setMinimumSize(QtCore.QSize(1366, 768))
        Form1.setMaximumSize(QtCore.QSize(1366, 768))
        self.pushButton = QtWidgets.QPushButton(Form1)
        self.pushButton.setGeometry(QtCore.QRect(730, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.treeWidget = QtWidgets.QTreeWidget(Form1)
        self.treeWidget.setGeometry(QtCore.QRect(40, 120, 371, 601))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.comboBox = QtWidgets.QComboBox(Form1)
        self.comboBox.setGeometry(QtCore.QRect(580, 120, 131, 21))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(Form1)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 190, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form1)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 230, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form1)
        self.label.setGeometry(QtCore.QRect(490, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(Form1)
        self.listView.setGeometry(QtCore.QRect(480, 180, 291, 241))
        self.listView.setObjectName("listView")
        self.pushButton_4 = QtWidgets.QPushButton(Form1)
        self.pushButton_4.setGeometry(QtCore.QRect(800, 460, 31, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listView_2 = QtWidgets.QListView(Form1)
        self.listView_2.setGeometry(QtCore.QRect(480, 450, 291, 241))
        self.listView_2.setObjectName("listView_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form1)
        self.pushButton_5.setGeometry(QtCore.QRect(800, 500, 31, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form1)
        self.pushButton_6.setGeometry(QtCore.QRect(1240, 190, 31, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.listView_3 = QtWidgets.QListView(Form1)
        self.listView_3.setGeometry(QtCore.QRect(920, 180, 291, 241))
        self.listView_3.setObjectName("listView_3")
        self.pushButton_7 = QtWidgets.QPushButton(Form1)
        self.pushButton_7.setGeometry(QtCore.QRect(1240, 460, 31, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.listView_4 = QtWidgets.QListView(Form1)
        self.listView_4.setGeometry(QtCore.QRect(920, 450, 291, 241))
        self.listView_4.setObjectName("listView_4")
        self.pushButton_8 = QtWidgets.QPushButton(Form1)
        self.pushButton_8.setGeometry(QtCore.QRect(1240, 500, 31, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form1)
        self.pushButton_9.setGeometry(QtCore.QRect(1240, 230, 31, 23))
        self.pushButton_9.setObjectName("pushButton_9")

        
        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "Form"))
        self.pushButton.setText(_translate("Form1", "查询"))
        self.pushButton_2.setText(_translate("Form1", "PushButton"))
        self.pushButton_3.setText(_translate("Form1", "PushButton"))
        self.label.setText(_translate("Form1", "药品名称："))
        self.pushButton_4.setText(_translate("Form1", "PushButton"))
        self.pushButton_5.setText(_translate("Form1", "PushButton"))
        self.pushButton_6.setText(_translate("Form1", "PushButton"))
        self.pushButton_7.setText(_translate("Form1", "PushButton"))
        self.pushButton_8.setText(_translate("Form1", "PushButton"))
        self.pushButton_9.setText(_translate("Form1", "PushButton"))


