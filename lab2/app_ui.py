# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\PyQt5\\Qt5\\plugins\\platforms'


class Ui_Database(object):
    def __init__(self, Database):
        Database.setObjectName("Database")
        Database.resize(825, 250)
        self.centralwidget = QtWidgets.QWidget(Database)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 40, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.table = QtWidgets.QComboBox(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(30, 50, 131, 41))
        self.table.setObjectName("table")
        self.table.addItem("")
        self.table.addItem("")
        self.table.addItem("")
        self.table.addItem("")
        self.table.addItem("")
        self.action = QtWidgets.QComboBox(self.centralwidget)
        self.action.setGeometry(QtCore.QRect(200, 50, 151, 41))
        self.action.setObjectName("action")
        self.action.addItem("")
        self.action.addItem("")
        self.action.addItem("")
        self.actLabel = QtWidgets.QLabel(self.centralwidget)
        self.actLabel.setGeometry(QtCore.QRect(30, 10, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.actLabel.setFont(font)
        self.actLabel.setObjectName("actLabel")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(360, 20, 321, 70))
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelSearch = QtWidgets.QLabel(self.centralwidget)
        self.labelSearch.setGeometry(QtCore.QRect(450, 230, 151, 31))
        self.labelSearch.setObjectName("labelSearch")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 300, 63, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(590, 180, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.info.setFont(font)
        self.info.setStyleSheet("color:green")
        self.info.setObjectName("info")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(20, 110, 751, 31))
        self.error.setStyleSheet("color:red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.gen_label = QtWidgets.QLabel(self.centralwidget)
        self.gen_label.setGeometry(QtCore.QRect(660, 320, 62, 19))
        self.gen_label.setText("")
        self.gen_label.setObjectName("gen_label")
        Database.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Database)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 26))
        self.menubar.setObjectName("menubar")
        Database.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Database)
        self.statusbar.setObjectName("statusbar")
        Database.setStatusBar(self.statusbar)

        self.retranslateUi(Database)
        QtCore.QMetaObject.connectSlotsByName(Database)

    def retranslateUi(self, Database):
        _translate = QtCore.QCoreApplication.translate
        Database.setWindowTitle(_translate("Database", "MainWindow"))
        self.pushButton.setText(_translate("Database", "Action"))
        self.table.setItemText(0, _translate("Database", "freelancer"))
        self.table.setItemText(1, _translate("Database", "project"))
        self.table.setItemText(2, _translate("Database", "task"))
        self.table.setItemText(3, _translate("Database", "client"))
        self.action.setItemText(0, _translate("Database", "delete"))
        self.action.setItemText(1, _translate("Database", "update"))
        self.action.setItemText(2, _translate("Database", "insert"))
        self.actLabel.setText(_translate("Database", "Choose table and action to do:"))
