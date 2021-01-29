# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uilogin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from uimain import *

class Ui_Login(QWidget):

    pass_signal = pyqtSignal()

    def __init__(self):
        # super这个用法是调用父类的构造函数
        # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
        super(Ui_Login, self).__init__()

        #self.setObjectName("Form")
        self.resize(600, 300)
        self.setMinimumSize(QtCore.QSize(600, 300))
        self.setMaximumSize(QtCore.QSize(600, 300))
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(350, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(350, 80, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("请输入账户")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 150, 181, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("请输入密码")
        #line_password = self.lineEdit_2.text()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录窗口"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "忘记密码"))

    #def closeEvent(self, event):

        #self.close_signal.emit()
        #self.close()

        # password = self.lineEdit_2.text()
        # if int(password) == 123456:
        #      #self.close_signal.emit()
        #     self.close()
        # else:
        #     reply = QMessageBox.warning(self, "警告", "账户或密码错误，请重新输入！")

    #def setupUi(self, Form):
    #     Form.setObjectName("Form")
    #     Form.resize(600, 300)
    #     Form.setMinimumSize(QtCore.QSize(600, 300))
    #     Form.setMaximumSize(QtCore.QSize(600, 300))
    #     self.pushButton = QtWidgets.QPushButton(Form)
    #     self.pushButton.setGeometry(QtCore.QRect(350, 230, 75, 23))
    #     self.pushButton.setObjectName("pushButton")
    #     #self.pushButton1 = QPushButton()
    #     self.pushButton_2 = QtWidgets.QPushButton(Form)
    #     self.pushButton_2.setGeometry(QtCore.QRect(460, 230, 75, 23))
    #     self.pushButton_2.setObjectName("pushButton_2")
    #     self.lineEdit = QtWidgets.QLineEdit(Form)
    #     self.lineEdit.setGeometry(QtCore.QRect(350, 80, 181, 31))
    #     self.lineEdit.setObjectName("lineEdit")
    #     self.lineEdit.setPlaceholderText("请输入账户")
    #     self.lineEdit_2 = QtWidgets.QLineEdit(Form)
    #     self.lineEdit_2.setGeometry(QtCore.QRect(350, 150, 181, 31))
    #     self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
    #     self.lineEdit_2.setObjectName("lineEdit_2")
    #     self.lineEdit_2.setPlaceholderText("请输入密码")
    #
    #     self.retranslateUi(Form)
    #     #self.pushButton.clicked.connect(lambda:self.login_fuc())
    #     self.pushButton.clicked.connect(Form.close)
    #     QtCore.QMetaObject.connectSlotsByName(Form)

    def login_fuc(self):

        password = self.lineEdit_2.text()
        if int(password) == 123456:
            self.pass_signal.emit()
            self.close()
            return 0
        else :
            reply = QMessageBox.warning(self, "警告", "账户或密码错误，请重新输入！")
            return 1