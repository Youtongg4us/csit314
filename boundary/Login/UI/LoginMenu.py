# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(1640, 830)
        loginWindow.setMinimumSize(QtCore.QSize(1200, 830))
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_picture = QtWidgets.QLabel(self.centralwidget)
        self.label_picture.setGeometry(QtCore.QRect(170, 100, 541, 641))
        self.label_picture.setStyleSheet("border-image: url(:/icons/icons/GPT_login_pic_daylight.webp);\n"
"border-top-left-radius:30;\n"
"border-bottom-left-radius:30px;")
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")
        self.label_input_layer = QtWidgets.QLabel(self.centralwidget)
        self.label_input_layer.setGeometry(QtCore.QRect(710, 100, 401, 641))
        self.label_input_layer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:30;\n"
"border-bottom-right-radius:30px;\n"
"")
        self.label_input_layer.setText("")
        self.label_input_layer.setObjectName("label_input_layer")
        self.label_introduce = QtWidgets.QLabel(self.centralwidget)
        self.label_introduce.setGeometry(QtCore.QRect(760, 180, 311, 111))
        self.label_introduce.setMinimumSize(QtCore.QSize(311, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_introduce.setFont(font)
        self.label_introduce.setObjectName("label_introduce")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(970, 110, 121, 51))
        self.frame.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_account = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_account.setGeometry(QtCore.QRect(740, 300, 161, 51))
        self.pushButton_account.setMinimumSize(QtCore.QSize(141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_account.setFont(font)
        self.pushButton_account.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    border:2px solid rgb(0, 0, 0);\n"
"\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:5pax;\n"
"    padding-left:5pax;\n"
"}")
        self.pushButton_account.setObjectName("pushButton_account")
        self.SlideAniStackedWidget = SlideAniStackedWidget(self.centralwidget)
        self.SlideAniStackedWidget.setGeometry(QtCore.QRect(740, 350, 335, 331))
        self.SlideAniStackedWidget.setObjectName("SlideAniStackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_username = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(311, 61))
        self.lineEdit_username.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(311, 61))
        self.lineEdit_password.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_login = QtWidgets.QPushButton(self.page_login)
        self.pushButton_login.setMinimumSize(QtCore.QSize(311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    border:2px solid rgb(0, 0, 0);\n"
"\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:5pax;\n"
"    padding-left:5pax;\n"
"}")
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout_2.addWidget(self.pushButton_login)
        self.SlideAniStackedWidget.addWidget(self.page_login)
        self.page_reg = QtWidgets.QWidget()
        self.page_reg.setObjectName("page_reg")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_reg)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_username_reg = QtWidgets.QLineEdit(self.page_reg)
        self.lineEdit_username_reg.setMinimumSize(QtCore.QSize(311, 61))
        self.lineEdit_username_reg.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);")
        self.lineEdit_username_reg.setObjectName("lineEdit_username_reg")
        self.verticalLayout_3.addWidget(self.lineEdit_username_reg)
        self.lineEdit_password_reg = QtWidgets.QLineEdit(self.page_reg)
        self.lineEdit_password_reg.setMinimumSize(QtCore.QSize(311, 61))
        self.lineEdit_password_reg.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);")
        self.lineEdit_password_reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_reg.setObjectName("lineEdit_password_reg")
        self.verticalLayout_3.addWidget(self.lineEdit_password_reg)
        self.lineEdit_email = QtWidgets.QLineEdit(self.page_reg)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(311, 61))
        self.lineEdit_email.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);")
        self.lineEdit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout_3.addWidget(self.lineEdit_email)
        self.ComboBox_type = ComboBox(self.page_reg)
        self.ComboBox_type.setObjectName("ComboBox_type")
        self.verticalLayout_3.addWidget(self.ComboBox_type)
        self.pushButton_reg = QtWidgets.QPushButton(self.page_reg)
        self.pushButton_reg.setMinimumSize(QtCore.QSize(311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_reg.setFont(font)
        self.pushButton_reg.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    border:2px solid rgb(0, 0, 0);\n"
"\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:5pax;\n"
"    padding-left:5pax;\n"
"}")
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.verticalLayout_3.addWidget(self.pushButton_reg)
        self.SlideAniStackedWidget.addWidget(self.page_reg)
        self.pushButton_Sign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sign.setGeometry(QtCore.QRect(910, 300, 161, 51))
        self.pushButton_Sign.setMinimumSize(QtCore.QSize(141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.pushButton_Sign.setFont(font)
        self.pushButton_Sign.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    border:2px solid rgb(0, 0, 0);\n"
"\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:5pax;\n"
"    padding-left:5pax;\n"
"}")
        self.pushButton_Sign.setObjectName("pushButton_Sign")
        self.label_input_layer.raise_()
        self.label_introduce.raise_()
        self.label_picture.raise_()
        self.frame.raise_()
        self.pushButton_account.raise_()
        self.SlideAniStackedWidget.raise_()
        self.pushButton_Sign.raise_()
        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWindow)
        self.SlideAniStackedWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(loginWindow.close) # type: ignore
        self.pushButton.clicked.connect(loginWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "MainWindow"))
        self.label_introduce.setText(_translate("loginWindow", "find your dream home"))
        self.pushButton_account.setText(_translate("loginWindow", "Have account"))
        self.lineEdit_username.setPlaceholderText(_translate("loginWindow", "Username"))
        self.lineEdit_password.setPlaceholderText(_translate("loginWindow", "Password"))
        self.pushButton_login.setText(_translate("loginWindow", "login"))
        self.lineEdit_username_reg.setPlaceholderText(_translate("loginWindow", "Username"))
        self.lineEdit_password_reg.setPlaceholderText(_translate("loginWindow", "Password"))
        self.lineEdit_email.setPlaceholderText(_translate("loginWindow", "email"))
        self.pushButton_reg.setText(_translate("loginWindow", "register"))
        self.pushButton_Sign.setText(_translate("loginWindow", "Sign up"))
from qfluentwidgets import ComboBox
from qfluentwidgetspro import SlideAniStackedWidget
import res_rc