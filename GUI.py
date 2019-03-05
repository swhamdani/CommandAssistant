# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CMDAssistantUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Command Assistant UI")
        Dialog.resize(734, 596)
        self.runHere = QtWidgets.QPushButton(Dialog)
        self.runHere.setGeometry(QtCore.QRect(450, 130, 91, 23))
        self.runHere.setObjectName("runHere")
        self.lineEditCmd = QtWidgets.QLineEdit(Dialog)
        self.lineEditCmd.setGeometry(QtCore.QRect(270, 130, 121, 20))
        self.lineEditCmd.setObjectName("lineEditCmd")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 130, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.runCMD = QtWidgets.QPushButton(Dialog)
        self.runCMD.setGeometry(QtCore.QRect(550, 130, 141, 23))
        self.runCMD.setObjectName("runCMD")
        self.clrButton = QtWidgets.QPushButton(Dialog)
        self.clrButton.setGeometry(QtCore.QRect(400, 130, 41, 23))
        self.clrButton.setObjectName("clrButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 30, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(150, 160, 541, 431))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CMDAssistant"))
        self.runHere.setText(_translate("Dialog", "Execute Here"))
        self.label_2.setText(_translate("Dialog", "Enter Command"))
        self.runCMD.setText(_translate("Dialog", "Execute on CMD Prompt"))
        self.clrButton.setText(_translate("Dialog", "Clear"))
        self.label.setText(_translate("Dialog", "Executing CMD Commands on Python"))
