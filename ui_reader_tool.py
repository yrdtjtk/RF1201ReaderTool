# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader_tool.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1535, 516)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_10.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_10.setSpacing(1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_9.setSpacing(1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lbl_Status = QtWidgets.QLabel(self.frame_3)
        self.lbl_Status.setObjectName("lbl_Status")
        self.gridLayout_9.addWidget(self.lbl_Status, 0, 0, 1, 1)
        self.lbl_Tip = QtWidgets.QLabel(self.frame_3)
        self.lbl_Tip.setObjectName("lbl_Tip")
        self.gridLayout_9.addWidget(self.lbl_Tip, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pb_RequestAll = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_RequestAll.sizePolicy().hasHeightForWidth())
        self.pb_RequestAll.setSizePolicy(sizePolicy)
        self.pb_RequestAll.setObjectName("pb_RequestAll")
        self.gridLayout.addWidget(self.pb_RequestAll, 4, 2, 1, 1)
        self.le_Csn = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Csn.sizePolicy().hasHeightForWidth())
        self.le_Csn.setSizePolicy(sizePolicy)
        self.le_Csn.setObjectName("le_Csn")
        self.gridLayout.addWidget(self.le_Csn, 4, 5, 1, 1)
        self.pb_Anticol = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Anticol.sizePolicy().hasHeightForWidth())
        self.pb_Anticol.setSizePolicy(sizePolicy)
        self.pb_Anticol.setObjectName("pb_Anticol")
        self.gridLayout.addWidget(self.pb_Anticol, 4, 4, 1, 1)
        self.pb_SelectCard = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_SelectCard.sizePolicy().hasHeightForWidth())
        self.pb_SelectCard.setSizePolicy(sizePolicy)
        self.pb_SelectCard.setObjectName("pb_SelectCard")
        self.gridLayout.addWidget(self.pb_SelectCard, 4, 6, 1, 1)
        self.le_Sak = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Sak.sizePolicy().hasHeightForWidth())
        self.le_Sak.setSizePolicy(sizePolicy)
        self.le_Sak.setObjectName("le_Sak")
        self.gridLayout.addWidget(self.le_Sak, 4, 7, 1, 1)
        self.le_CpuPpsRecv = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_CpuPpsRecv.sizePolicy().hasHeightForWidth())
        self.le_CpuPpsRecv.setSizePolicy(sizePolicy)
        self.le_CpuPpsRecv.setObjectName("le_CpuPpsRecv")
        self.gridLayout.addWidget(self.le_CpuPpsRecv, 11, 9, 1, 1)
        self.pb_HaltCard = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_HaltCard.sizePolicy().hasHeightForWidth())
        self.pb_HaltCard.setSizePolicy(sizePolicy)
        self.pb_HaltCard.setObjectName("pb_HaltCard")
        self.gridLayout.addWidget(self.pb_HaltCard, 4, 9, 1, 1)
        self.pb_FoundCard = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_FoundCard.sizePolicy().hasHeightForWidth())
        self.pb_FoundCard.setSizePolicy(sizePolicy)
        self.pb_FoundCard.setObjectName("pb_FoundCard")
        self.gridLayout.addWidget(self.pb_FoundCard, 4, 8, 1, 1)
        self.pb_Beep = QtWidgets.QPushButton(Form)
        self.pb_Beep.setObjectName("pb_Beep")
        self.gridLayout.addWidget(self.pb_Beep, 1, 5, 1, 1)
        self.pb_WriteBlock = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_WriteBlock.sizePolicy().hasHeightForWidth())
        self.pb_WriteBlock.setSizePolicy(sizePolicy)
        self.pb_WriteBlock.setObjectName("pb_WriteBlock")
        self.gridLayout.addWidget(self.pb_WriteBlock, 5, 6, 1, 1)
        self.pb_ReadBlock = QtWidgets.QPushButton(Form)
        self.pb_ReadBlock.setObjectName("pb_ReadBlock")
        self.gridLayout.addWidget(self.pb_ReadBlock, 5, 3, 1, 1)
        self.le_ReadBlock = QtWidgets.QLineEdit(Form)
        self.le_ReadBlock.setObjectName("le_ReadBlock")
        self.gridLayout.addWidget(self.le_ReadBlock, 5, 4, 1, 2)
        self.le_WriteBlock = QtWidgets.QLineEdit(Form)
        self.le_WriteBlock.setObjectName("le_WriteBlock")
        self.gridLayout.addWidget(self.le_WriteBlock, 5, 7, 1, 2)
        self.le_CosRetData = QtWidgets.QLineEdit(Form)
        self.le_CosRetData.setObjectName("le_CosRetData")
        self.gridLayout.addWidget(self.le_CosRetData, 10, 3, 1, 9)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 1, 1, 1)
        self.pb_CpuDeselect = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_CpuDeselect.sizePolicy().hasHeightForWidth())
        self.pb_CpuDeselect.setSizePolicy(sizePolicy)
        self.pb_CpuDeselect.setObjectName("pb_CpuDeselect")
        self.gridLayout.addWidget(self.pb_CpuDeselect, 8, 11, 1, 1)
        self.pb_LoadKeyB = QtWidgets.QPushButton(Form)
        self.pb_LoadKeyB.setObjectName("pb_LoadKeyB")
        self.gridLayout.addWidget(self.pb_LoadKeyB, 7, 4, 1, 1)
        self.pb_AuthKeyA = QtWidgets.QPushButton(Form)
        self.pb_AuthKeyA.setObjectName("pb_AuthKeyA")
        self.gridLayout.addWidget(self.pb_AuthKeyA, 6, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1)
        self.pb_AuthKeyB = QtWidgets.QPushButton(Form)
        self.pb_AuthKeyB.setObjectName("pb_AuthKeyB")
        self.gridLayout.addWidget(self.pb_AuthKeyB, 7, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)
        self.le_KeyA = QtWidgets.QLineEdit(Form)
        self.le_KeyA.setObjectName("le_KeyA")
        self.gridLayout.addWidget(self.le_KeyA, 6, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.cob_BlockNo = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cob_BlockNo.setFont(font)
        self.cob_BlockNo.setObjectName("cob_BlockNo")
        self.gridLayout.addWidget(self.cob_BlockNo, 5, 2, 1, 1)
        self.pb_LoadKeyA = QtWidgets.QPushButton(Form)
        self.pb_LoadKeyA.setObjectName("pb_LoadKeyA")
        self.gridLayout.addWidget(self.pb_LoadKeyA, 6, 4, 1, 1)
        self.le_KeyB = QtWidgets.QLineEdit(Form)
        self.le_KeyB.setObjectName("le_KeyB")
        self.gridLayout.addWidget(self.le_KeyB, 7, 2, 1, 2)
        self.cob_SamBaudrate = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cob_SamBaudrate.sizePolicy().hasHeightForWidth())
        self.cob_SamBaudrate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cob_SamBaudrate.setFont(font)
        self.cob_SamBaudrate.setObjectName("cob_SamBaudrate")
        self.gridLayout.addWidget(self.cob_SamBaudrate, 8, 6, 1, 1)
        self.cob_SamSlot = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cob_SamSlot.sizePolicy().hasHeightForWidth())
        self.cob_SamSlot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cob_SamSlot.setFont(font)
        self.cob_SamSlot.setObjectName("cob_SamSlot")
        self.gridLayout.addWidget(self.cob_SamSlot, 8, 4, 1, 1)
        self.pb_SelectSamBaudrate = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_SelectSamBaudrate.sizePolicy().hasHeightForWidth())
        self.pb_SelectSamBaudrate.setSizePolicy(sizePolicy)
        self.pb_SelectSamBaudrate.setObjectName("pb_SelectSamBaudrate")
        self.gridLayout.addWidget(self.pb_SelectSamBaudrate, 8, 5, 1, 1)
        self.pb_ReadSid = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ReadSid.sizePolicy().hasHeightForWidth())
        self.pb_ReadSid.setSizePolicy(sizePolicy)
        self.pb_ReadSid.setObjectName("pb_ReadSid")
        self.gridLayout.addWidget(self.pb_ReadSid, 11, 1, 1, 1)
        self.le_ReadSid = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_ReadSid.sizePolicy().hasHeightForWidth())
        self.le_ReadSid.setSizePolicy(sizePolicy)
        self.le_ReadSid.setObjectName("le_ReadSid")
        self.gridLayout.addWidget(self.le_ReadSid, 11, 2, 1, 1)
        self.pb_ReadLkt4210Info = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ReadLkt4210Info.sizePolicy().hasHeightForWidth())
        self.pb_ReadLkt4210Info.setSizePolicy(sizePolicy)
        self.pb_ReadLkt4210Info.setObjectName("pb_ReadLkt4210Info")
        self.gridLayout.addWidget(self.pb_ReadLkt4210Info, 11, 3, 1, 1)
        self.le_ReadLkt4210Info = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_ReadLkt4210Info.sizePolicy().hasHeightForWidth())
        self.le_ReadLkt4210Info.setSizePolicy(sizePolicy)
        self.le_ReadLkt4210Info.setObjectName("le_ReadLkt4210Info")
        self.gridLayout.addWidget(self.le_ReadLkt4210Info, 11, 4, 1, 1)
        self.pb_RfReset = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_RfReset.sizePolicy().hasHeightForWidth())
        self.pb_RfReset.setSizePolicy(sizePolicy)
        self.pb_RfReset.setObjectName("pb_RfReset")
        self.gridLayout.addWidget(self.pb_RfReset, 11, 5, 1, 1)
        self.le_RfResetMs = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_RfResetMs.sizePolicy().hasHeightForWidth())
        self.le_RfResetMs.setSizePolicy(sizePolicy)
        self.le_RfResetMs.setObjectName("le_RfResetMs")
        self.gridLayout.addWidget(self.le_RfResetMs, 11, 6, 1, 1)
        self.pb_CpuPps = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_CpuPps.sizePolicy().hasHeightForWidth())
        self.pb_CpuPps.setSizePolicy(sizePolicy)
        self.pb_CpuPps.setObjectName("pb_CpuPps")
        self.gridLayout.addWidget(self.pb_CpuPps, 11, 7, 1, 1)
        self.le_CpuPpsSend = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_CpuPpsSend.sizePolicy().hasHeightForWidth())
        self.le_CpuPpsSend.setSizePolicy(sizePolicy)
        self.le_CpuPpsSend.setObjectName("le_CpuPpsSend")
        self.gridLayout.addWidget(self.le_CpuPpsSend, 11, 8, 1, 1)
        self.te_Recv = QtWidgets.QTextEdit(Form)
        self.te_Recv.setObjectName("te_Recv")
        self.gridLayout.addWidget(self.te_Recv, 0, 1, 1, 12)
        self.le_Atqa = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Atqa.sizePolicy().hasHeightForWidth())
        self.le_Atqa.setSizePolicy(sizePolicy)
        self.le_Atqa.setObjectName("le_Atqa")
        self.gridLayout.addWidget(self.le_Atqa, 4, 3, 1, 1)
        self.pb_Request = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Request.sizePolicy().hasHeightForWidth())
        self.pb_Request.setSizePolicy(sizePolicy)
        self.pb_Request.setObjectName("pb_Request")
        self.gridLayout.addWidget(self.pb_Request, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(100, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 12, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_8.setSpacing(1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSpacing(1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 1, 1, 1, 1)
        self.lbl_Com = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Com.sizePolicy().hasHeightForWidth())
        self.lbl_Com.setSizePolicy(sizePolicy)
        self.lbl_Com.setObjectName("lbl_Com")
        self.gridLayout_7.addWidget(self.lbl_Com, 1, 0, 1, 1)
        self.cob_Com = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cob_Com.sizePolicy().hasHeightForWidth())
        self.cob_Com.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cob_Com.setFont(font)
        self.cob_Com.setObjectName("cob_Com")
        self.gridLayout_7.addWidget(self.cob_Com, 1, 2, 1, 1)
        self.pb_OpenOrClose = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_OpenOrClose.sizePolicy().hasHeightForWidth())
        self.pb_OpenOrClose.setSizePolicy(sizePolicy)
        self.pb_OpenOrClose.setObjectName("pb_OpenOrClose")
        self.gridLayout_7.addWidget(self.pb_OpenOrClose, 1, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 3)
        self.pb_ClearRecv = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ClearRecv.sizePolicy().hasHeightForWidth())
        self.pb_ClearRecv.setSizePolicy(sizePolicy)
        self.pb_ClearRecv.setObjectName("pb_ClearRecv")
        self.gridLayout.addWidget(self.pb_ClearRecv, 1, 4, 1, 1)
        self.cob_Channel = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cob_Channel.sizePolicy().hasHeightForWidth())
        self.cob_Channel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cob_Channel.setFont(font)
        self.cob_Channel.setObjectName("cob_Channel")
        self.gridLayout.addWidget(self.cob_Channel, 8, 2, 1, 1)
        self.pb_SelectSamSlot = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_SelectSamSlot.sizePolicy().hasHeightForWidth())
        self.pb_SelectSamSlot.setSizePolicy(sizePolicy)
        self.pb_SelectSamSlot.setObjectName("pb_SelectSamSlot")
        self.gridLayout.addWidget(self.pb_SelectSamSlot, 8, 3, 1, 1)
        self.pb_CosCmd = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_CosCmd.sizePolicy().hasHeightForWidth())
        self.pb_CosCmd.setSizePolicy(sizePolicy)
        self.pb_CosCmd.setObjectName("pb_CosCmd")
        self.gridLayout.addWidget(self.pb_CosCmd, 9, 1, 1, 1)
        self.pb_CpuReset = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_CpuReset.sizePolicy().hasHeightForWidth())
        self.pb_CpuReset.setSizePolicy(sizePolicy)
        self.pb_CpuReset.setObjectName("pb_CpuReset")
        self.gridLayout.addWidget(self.pb_CpuReset, 8, 7, 1, 1)
        self.le_CpuReset = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_CpuReset.sizePolicy().hasHeightForWidth())
        self.le_CpuReset.setSizePolicy(sizePolicy)
        self.le_CpuReset.setObjectName("le_CpuReset")
        self.gridLayout.addWidget(self.le_CpuReset, 8, 8, 1, 3)
        self.le_CosCmd = QtWidgets.QLineEdit(Form)
        self.le_CosCmd.setObjectName("le_CosCmd")
        self.gridLayout.addWidget(self.le_CosCmd, 9, 2, 1, 10)
        self.le_CosRetCode = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_CosRetCode.sizePolicy().hasHeightForWidth())
        self.le_CosRetCode.setSizePolicy(sizePolicy)
        self.le_CosRetCode.setObjectName("le_CosRetCode")
        self.gridLayout.addWidget(self.le_CosRetCode, 10, 2, 1, 1)
        self.le_IncValue = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_IncValue.sizePolicy().hasHeightForWidth())
        self.le_IncValue.setSizePolicy(sizePolicy)
        self.le_IncValue.setObjectName("le_IncValue")
        self.gridLayout.addWidget(self.le_IncValue, 6, 9, 1, 1)
        self.le_ReadValue = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_ReadValue.sizePolicy().hasHeightForWidth())
        self.le_ReadValue.setSizePolicy(sizePolicy)
        self.le_ReadValue.setObjectName("le_ReadValue")
        self.gridLayout.addWidget(self.le_ReadValue, 6, 7, 1, 1)
        self.le_WriteValue = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_WriteValue.sizePolicy().hasHeightForWidth())
        self.le_WriteValue.setSizePolicy(sizePolicy)
        self.le_WriteValue.setObjectName("le_WriteValue")
        self.gridLayout.addWidget(self.le_WriteValue, 7, 7, 1, 1)
        self.pb_ReadValue = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ReadValue.sizePolicy().hasHeightForWidth())
        self.pb_ReadValue.setSizePolicy(sizePolicy)
        self.pb_ReadValue.setObjectName("pb_ReadValue")
        self.gridLayout.addWidget(self.pb_ReadValue, 6, 6, 1, 1)
        self.pb_WriteValue = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_WriteValue.sizePolicy().hasHeightForWidth())
        self.pb_WriteValue.setSizePolicy(sizePolicy)
        self.pb_WriteValue.setObjectName("pb_WriteValue")
        self.gridLayout.addWidget(self.pb_WriteValue, 7, 6, 1, 1)
        self.le_TransferBlockNo = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_TransferBlockNo.sizePolicy().hasHeightForWidth())
        self.le_TransferBlockNo.setSizePolicy(sizePolicy)
        self.le_TransferBlockNo.setObjectName("le_TransferBlockNo")
        self.gridLayout.addWidget(self.le_TransferBlockNo, 7, 11, 1, 1)
        self.pb_Restore = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Restore.sizePolicy().hasHeightForWidth())
        self.pb_Restore.setSizePolicy(sizePolicy)
        self.pb_Restore.setObjectName("pb_Restore")
        self.gridLayout.addWidget(self.pb_Restore, 6, 10, 1, 1)
        self.pb_Transfer = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Transfer.sizePolicy().hasHeightForWidth())
        self.pb_Transfer.setSizePolicy(sizePolicy)
        self.pb_Transfer.setObjectName("pb_Transfer")
        self.gridLayout.addWidget(self.pb_Transfer, 7, 10, 1, 1)
        self.le_DecValue = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_DecValue.sizePolicy().hasHeightForWidth())
        self.le_DecValue.setSizePolicy(sizePolicy)
        self.le_DecValue.setObjectName("le_DecValue")
        self.gridLayout.addWidget(self.le_DecValue, 7, 9, 1, 1)
        self.pb_DecValue = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_DecValue.sizePolicy().hasHeightForWidth())
        self.pb_DecValue.setSizePolicy(sizePolicy)
        self.pb_DecValue.setObjectName("pb_DecValue")
        self.gridLayout.addWidget(self.pb_DecValue, 7, 8, 1, 1)
        self.pb_IncValue = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_IncValue.sizePolicy().hasHeightForWidth())
        self.pb_IncValue.setSizePolicy(sizePolicy)
        self.pb_IncValue.setObjectName("pb_IncValue")
        self.gridLayout.addWidget(self.pb_IncValue, 6, 8, 1, 1)
        self.pb_SelectChannel = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_SelectChannel.sizePolicy().hasHeightForWidth())
        self.pb_SelectChannel.setSizePolicy(sizePolicy)
        self.pb_SelectChannel.setObjectName("pb_SelectChannel")
        self.gridLayout.addWidget(self.pb_SelectChannel, 8, 1, 1, 1)
        self.le_RestoreBlockNo = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_RestoreBlockNo.sizePolicy().hasHeightForWidth())
        self.le_RestoreBlockNo.setSizePolicy(sizePolicy)
        self.le_RestoreBlockNo.setObjectName("le_RestoreBlockNo")
        self.gridLayout.addWidget(self.le_RestoreBlockNo, 6, 11, 1, 1)
        self.pb_CalcKeyBs = QtWidgets.QPushButton(Form)
        self.pb_CalcKeyBs.setObjectName("pb_CalcKeyBs")
        self.gridLayout.addWidget(self.pb_CalcKeyBs, 12, 1, 1, 1)
        self.pb_ReadAllBlocks = QtWidgets.QPushButton(Form)
        self.pb_ReadAllBlocks.setObjectName("pb_ReadAllBlocks")
        self.gridLayout.addWidget(self.pb_ReadAllBlocks, 12, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Serial Tool"))
        self.lbl_Status.setText(_translate("Form", "TextLabel"))
        self.lbl_Tip.setText(_translate("Form", "TextLabel"))
        self.pb_RequestAll.setText(_translate("Form", "Request All"))
        self.pb_Anticol.setText(_translate("Form", "Anticollision"))
        self.pb_SelectCard.setText(_translate("Form", "SelectCard"))
        self.pb_HaltCard.setText(_translate("Form", "Halt Card"))
        self.pb_FoundCard.setText(_translate("Form", "Found Card"))
        self.pb_Beep.setText(_translate("Form", "Beep"))
        self.pb_WriteBlock.setText(_translate("Form", "Write Block"))
        self.pb_ReadBlock.setText(_translate("Form", "Read Block"))
        self.label_5.setText(_translate("Form", "COS Return:"))
        self.pb_CpuDeselect.setText(_translate("Form", "CPU Deselect"))
        self.pb_LoadKeyB.setText(_translate("Form", "Load KeyB"))
        self.pb_AuthKeyA.setText(_translate("Form", "Auth KeyA"))
        self.label_3.setText(_translate("Form", "Key A:"))
        self.pb_AuthKeyB.setText(_translate("Form", "Auth KeyB"))
        self.label_4.setText(_translate("Form", "Key B:"))
        self.label_2.setText(_translate("Form", "Block No:"))
        self.pb_LoadKeyA.setText(_translate("Form", "Load KeyA"))
        self.pb_SelectSamBaudrate.setText(_translate("Form", "Select Sam Baudrate"))
        self.pb_ReadSid.setText(_translate("Form", "Read SID"))
        self.pb_ReadLkt4210Info.setText(_translate("Form", "Read LKT4210 Info"))
        self.pb_RfReset.setText(_translate("Form", "RF Reset"))
        self.pb_CpuPps.setText(_translate("Form", "CPU PPS"))
        self.pb_Request.setText(_translate("Form", "Request"))
        self.label.setText(_translate("Form", "Port No:"))
        self.lbl_Com.setText(_translate("Form", "TextLabel"))
        self.pb_OpenOrClose.setText(_translate("Form", "打开(&O)"))
        self.pb_ClearRecv.setText(_translate("Form", "Clear Recv"))
        self.pb_SelectSamSlot.setText(_translate("Form", "Select Sam Slot"))
        self.pb_CosCmd.setText(_translate("Form", "COS Cmd"))
        self.pb_CpuReset.setText(_translate("Form", "CPU Reset"))
        self.pb_ReadValue.setText(_translate("Form", "Read Value"))
        self.pb_WriteValue.setText(_translate("Form", "Write Value"))
        self.pb_Restore.setText(_translate("Form", "Restore"))
        self.pb_Transfer.setText(_translate("Form", "Transfer"))
        self.pb_DecValue.setText(_translate("Form", "Dec Value"))
        self.pb_IncValue.setText(_translate("Form", "Inc Value"))
        self.pb_SelectChannel.setText(_translate("Form", "Select Channel"))
        self.pb_CalcKeyBs.setText(_translate("Form", "CalcKeyBs"))
        self.pb_ReadAllBlocks.setText(_translate("Form", "Read All Blocks"))

