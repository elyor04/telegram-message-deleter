# Form implementation generated from reading ui file '/Users/elyor/Documents/qt-projects/tg-app-ui/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 361, 241))
        self.groupBox.setStyleSheet("font: 18pt;")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 291, 183))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.password.setEnabled(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.number = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.number.setObjectName("number")
        self.gridLayout.addWidget(self.number, 0, 1, 1, 1)
        self.pswdCheck = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.pswdCheck.setObjectName("pswdCheck")
        self.gridLayout.addWidget(self.pswdCheck, 2, 0, 1, 1)
        self.loginInfo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.loginInfo.setObjectName("loginInfo")
        self.gridLayout.addWidget(self.loginInfo, 3, 1, 1, 1)
        self.loginBut = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.loginBut.setObjectName("loginBut")
        self.gridLayout.addWidget(self.loginBut, 3, 0, 1, 1)
        self.code = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.code.setEnabled(False)
        self.code.setObjectName("code")
        self.gridLayout.addWidget(self.code, 1, 1, 1, 1)
        self.refreshBut = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.refreshBut.setObjectName("refreshBut")
        self.gridLayout.addWidget(self.refreshBut, 4, 0, 1, 1)
        self.deleteBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.deleteBox.setEnabled(False)
        self.deleteBox.setGeometry(QtCore.QRect(420, 20, 351, 241))
        self.deleteBox.setStyleSheet("font: 18pt;")
        self.deleteBox.setObjectName("deleteBox")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.deleteBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 271, 142))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.deleteInfo = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.deleteInfo.setObjectName("deleteInfo")
        self.gridLayout_2.addWidget(self.deleteInfo, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.ending = QtWidgets.QDateEdit(parent=self.layoutWidget_2)
        self.ending.setObjectName("ending")
        self.gridLayout_2.addWidget(self.ending, 1, 1, 1, 1)
        self.starting = QtWidgets.QDateEdit(parent=self.layoutWidget_2)
        self.starting.setObjectName("starting")
        self.gridLayout_2.addWidget(self.starting, 0, 1, 1, 1)
        self.deleteBut = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.deleteBut.setObjectName("deleteBut")
        self.gridLayout_2.addWidget(self.deleteBut, 3, 0, 1, 1)
        self.pChatsCheck = QtWidgets.QCheckBox(parent=self.layoutWidget_2)
        self.pChatsCheck.setObjectName("pChatsCheck")
        self.gridLayout_2.addWidget(self.pChatsCheck, 2, 0, 1, 1)
        self.groupsCheck = QtWidgets.QCheckBox(parent=self.layoutWidget_2)
        self.groupsCheck.setObjectName("groupsCheck")
        self.gridLayout_2.addWidget(self.groupsCheck, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 280, 631, 241))
        self.groupBox_3.setStyleSheet("font: 18pt;")
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 30, 611, 201))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.usrPhoto = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.usrPhoto.setStyleSheet("background: rgb(150, 150, 150);")
        self.usrPhoto.setObjectName("usrPhoto")
        self.gridLayout_3.addWidget(self.usrPhoto, 0, 0, 4, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)
        self.usrName = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.usrName.setObjectName("usrName")
        self.gridLayout_3.addWidget(self.usrName, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 1)
        self.usrNum = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.usrNum.setObjectName("usrNum")
        self.gridLayout_3.addWidget(self.usrNum, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 1, 1, 1)
        self.usrUsrname = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.usrUsrname.setObjectName("usrUsrname")
        self.gridLayout_3.addWidget(self.usrUsrname, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Phone number:"))
        self.label_2.setText(_translate("MainWindow", "Code:"))
        self.pswdCheck.setText(_translate("MainWindow", "Password:"))
        self.loginBut.setText(_translate("MainWindow", "Ok"))
        self.refreshBut.setText(_translate("MainWindow", "Refresh"))
        self.deleteBox.setTitle(_translate("MainWindow", "Delete"))
        self.label_5.setText(_translate("MainWindow", "Ending date:"))
        self.label_4.setText(_translate("MainWindow", "Starting date:"))
        self.deleteBut.setText(_translate("MainWindow", "Ok"))
        self.pChatsCheck.setText(_translate("MainWindow", "Private Chats"))
        self.groupsCheck.setText(_translate("MainWindow", "Groups"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Profile"))
        self.label_7.setText(_translate("MainWindow", "Name:"))
        self.label_8.setText(_translate("MainWindow", "Phone number:"))
        self.label_9.setText(_translate("MainWindow", "Username:"))