# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'k:\d\MyProjects\Python\RF1201_Reader_Tool\cpu_consume.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1208, 895)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pb_Consume = QtWidgets.QPushButton(Dialog)
        self.pb_Consume.setObjectName("pb_Consume")
        self.gridLayout.addWidget(self.pb_Consume, 2, 0, 1, 1)
        self.pb_ClearLog = QtWidgets.QPushButton(Dialog)
        self.pb_ClearLog.setObjectName("pb_ClearLog")
        self.gridLayout.addWidget(self.pb_ClearLog, 2, 1, 1, 1)
        self.te_Log = QtWidgets.QTextEdit(Dialog)
        self.te_Log.setObjectName("te_Log")
        self.gridLayout.addWidget(self.te_Log, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pb_Consume.setText(_translate("Dialog", "Consume"))
        self.pb_ClearLog.setText(_translate("Dialog", "Clear Log"))

