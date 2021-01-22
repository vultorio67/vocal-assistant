# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 280, 291, 81))
        self.label.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"            border-style: outset;\n"
"            border-width: 6px;\n"
"            border-radius: 10px;\n"
"border-color: rgb(170, 0, 127);\n"
"            font: bold 14px;\n"
"            min-width: 10em;\n"
"            padding: 6px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.me = QtWidgets.QLineEdit(self.centralwidget)
        self.me.setGeometry(QtCore.QRect(120, 170, 291, 81))
        self.me.setStyleSheet("            background-color: #610B0B;\n"
"            border-style: outset;\n"
"            border-width: 5px;\n"
"            border-radius: 10px;\n"
"border-color: rgb(85, 170, 127);\n"
"            font: bold 14px;\n"
"")
        self.me.setObjectName("me")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 201, 71))
        self.label_2.setStyleSheet("color: rgb(78, 140, 255);\n"
"border-color: rgb(12, 170, 218);\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"background-color: rgb(150, 0, 100);\n"
"border-radius: 10px;\n"
"font: bold 35px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(170, 420, 181, 61))
        self.b1.setStyleSheet("color: rgb(85, 170, 0);\n"
"            background-color: #0B4C5F;\n"
"            border-style: outset;\n"
"            border-width: 4px;\n"
"            border-radius: 10px;\n"
"            border-color: #2E2E2E;\n"
"            font: bold 17px;")
        self.b1.setObjectName("b1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "SWI"))
        self.b1.setText(_translate("MainWindow", "Speak"))


