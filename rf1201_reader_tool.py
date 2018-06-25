# -*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer
from ui_reader_tool import Ui_Form
from PyQt5.QtWidgets import QMessageBox

import time
import datetime

from reader import Reader
import serial.tools.list_ports

import threading

import func
from res import images_qr

from crypt import *


def getProgVer():
    return 'V1.003'


def getNowStr(isCompact=True, isMill=False):
    now = datetime.datetime.now()
    if isCompact:
        if isMill:
            s_datatime = now.strftime('%Y%m%d%H%M%S%f')
        else:
            s_datatime = now.strftime('%Y%m%d%H%M%S')
    else:
        if isMill:
            s_datatime = now.strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            s_datatime = now.strftime('%Y-%m-%d %H:%M:%S')
    return s_datatime


def getTxt(txtName):
    table = {'openPort': 'Open(&O)', 'closePort': 'Close(&C)'}
    return table[txtName]


# def createSerial(portName, baudrate):
#     ser = serial.Serial()
#     ser.port = portName
#     ser.baudrate = baudrate
#     ser.timeout = 2
#     ser.parity = 'N'
#     ser.stopbits = 1

#     return ser


# def portRecvProc(ser, sig):
#     while ser.isOpen():
#         try:
#             num = ser.inWaiting()
#             if num > 0:
#                 b = ser.read(num)
#                 sig.emit(b)
#         except Exception as e:
#             print(str(e))
#             ser.close()
#             return
#         time.sleep(0.01)


''' calcCardKeyBs
    return type:bytes length:6
'''
def calcCardKeyBs(reader):
    deskey = 'd463fee0c70007d598d4777badde94b0'
    loop = 0
    sec1keya = ''
    while True:
        r = reader.FoundCard()
        if not r or not func.IsSwOk(r[1]):
            return False
        csn = r[2][6:]
        baCsn = bytes.fromhex(csn)
        if loop == 0:
            sec1keya = 'FF' * 6
        elif loop == 1:
            sec1keya = '00' * 6
        else:
            sec1keya = csn + csn[0:4]
        reader.LoadKey(1, 1, sec1keya)
        r = reader.AuthKey(1, 1)
        if not func.IsSwOk(r[1]):
            loop += 1
            if loop > 2:
                return False
            continue
        r = reader.ReadBlock(4)
        if not func.IsSwOk(r[1]):
            return False
        block4 = bytes.fromhex(r[2])
        break
    KeyBs = list(range(16))
    if loop == 0:
        for i in range(16):
            KeyBs[i] = b'\xFF' * 6
    else:
        cardtype = block4[13]
        factor = bytearray(8)
        for i in range(4):
            factor[i] = baCsn[i]
        for i in range(3):
            factor[4+i] = block4[6+i]
        if 0x90==cardtype or 0x91==cardtype or 0x92==cardtype:
            for i in range(0,3):
                factor[7] = i
                KeyBs[i] = des_ecb(bytes(factor), deskey)
            for i in range(3,16):
                KeyBs[i] = KeyBs[2]
        else:
            for i in range(16):
                if i == 2:
                    factor[7] = 0x10
                elif i >= 3 and i <= 5:
                    factor[7] = 0x03
                elif i >= 7 and i <= 15:
                    factor[7] = i + 10
                else:
                    factor[7] = i
                KeyBs[i] = des_ecb(bytes(factor), deskey)
    return tuple(map(lambda x: x[0:6], KeyBs))





class MainWindow(QtWidgets.QWidget):

    sig_portRecv = QtCore.pyqtSignal(bytes, name='refresh_UI_Recv_Signal')

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.t = None


        self.setWindowTitle('RF1201 Card Reader Tool - ' + getProgVer())

        for port in serial.tools.list_ports.comports():
            self.ui.cob_Com.addItem(port[0])
        self.reader = Reader(self.ui.cob_Com.currentText())
        # self.ui.pb_OpenOrClose.setAttribute(Qt.WA_NativeWindow)
        self.ui.pb_OpenOrClose.setText(getTxt('openPort'))
        # self.ui.lbl_Com.setPixmap(QtGui.QPixmap("ico/off.png"))
        self.ui.lbl_Com.setPixmap(QtGui.QPixmap(":/ico/off.png"))
        self.ui.te_Recv.setReadOnly(True)
        self.ui.lbl_Status.setText('')
        self.ui.lbl_Tip.setText('')

        for x in range(0, 64):
            self.ui.cob_BlockNo.addItem('%02d' % x)

        self.ui.cob_Channel.addItem('Contactless Card')
        self.ui.cob_Channel.addItem('CPU Card')
        self.ui.cob_Channel.addItem('SAM Card')

        for x in range(3):
            self.ui.cob_SamSlot.addItem('Slot %d' %x)

        self.ui.cob_SamBaudrate.addItem('9600')
        self.ui.cob_SamBaudrate.addItem('38400')
        self.ui.cob_SamBaudrate.addItem('19200')
        self.ui.cob_SamBaudrate.addItem('56000')
        self.ui.cob_SamBaudrate.addItem('115200')

        self.ui.le_KeyA.setText('A0A1A2A3A4A5')
        self.ui.le_KeyB.setText('FFFFFFFFFFFF')

        self.ui.le_RfResetMs.setText('1')

        self.ui.le_WriteBlock.setMaxLength(32)
        self.ui.le_KeyA.setMaxLength(12)
        self.ui.le_KeyB.setMaxLength(12)

        self.timerTip = QTimer(self)
        self.timerTip.timeout.connect(self.timerTipProc)

        self.ui.pb_OpenOrClose.clicked.connect(self.on_pb_OpenOrClose_Clicked)
        self.ui.cob_Com.currentIndexChanged.connect(
            self.on_cob_Com_CurrentIndexChanged)
        self.ui.pb_ClearRecv.clicked.connect(self.on_pb_ClearRecv_Clicked)
        self.ui.pb_Beep.clicked.connect(self.on_pb_Beep)
        self.ui.pb_Request.clicked.connect(self.on_pb_Request)
        self.ui.pb_RequestAll.clicked.connect(self.on_pb_RequestAll)
        self.ui.pb_Anticol.clicked.connect(self.on_pb_Anticol)
        self.ui.pb_SelectCard.clicked.connect(self.on_pb_SelectCard)
        self.ui.pb_FoundCard.clicked.connect(self.on_pb_FoundCard)
        self.ui.pb_HaltCard.clicked.connect(self.on_pb_HaltCard)
        self.ui.pb_ReadBlock.clicked.connect(self.on_pb_ReadBlock)
        self.ui.pb_WriteBlock.clicked.connect(self.on_pb_WriteBlock)
        self.ui.pb_LoadKeyA.clicked.connect(self.on_pb_LoadKeyA)
        self.ui.pb_AuthKeyA.clicked.connect(self.on_pb_AuthKeyA)
        self.ui.pb_LoadKeyB.clicked.connect(self.on_pb_LoadKeyB)
        self.ui.pb_AuthKeyB.clicked.connect(self.on_pb_AuthKeyB)
        self.ui.pb_ReadValue.clicked.connect(self.on_pb_ReadValue)
        self.ui.pb_WriteValue.clicked.connect(self.on_pb_WriteValue)
        self.ui.pb_IncValue.clicked.connect(self.on_pb_IncValue)
        self.ui.pb_DecValue.clicked.connect(self.on_pb_DecValue)
        self.ui.pb_Restore.clicked.connect(self.on_pb_Restore)
        self.ui.pb_Transfer.clicked.connect(self.on_pb_Transfer)
        self.ui.pb_SelectChannel.clicked.connect(self.on_pb_SelectChannel)
        self.ui.pb_SelectSamSlot.clicked.connect(self.on_pb_SelectSamSlot)
        self.ui.pb_SelectSamBaudrate.clicked.connect(self.on_pb_SelectSamBaudrate)
        self.ui.pb_CpuReset.clicked.connect(self.on_pb_CpuReset)
        self.ui.pb_CpuDeselect.clicked.connect(self.on_pb_CpuDeselect)
        self.ui.pb_CosCmd.clicked.connect(self.on_pb_CosCmd)
        self.ui.pb_ReadSid.clicked.connect(self.on_pb_ReadSid)
        self.ui.pb_ReadLkt4210Info.clicked.connect(self.on_pb_ReadLkt4210Info)
        self.ui.pb_RfReset.clicked.connect(self.on_pb_RfReset)
        self.ui.pb_CpuPps.clicked.connect(self.on_pb_CpuPps)
        self.ui.pb_CalcKeyBs.clicked.connect(self.on_pb_CalcKeyBs)
        self.ui.pb_ReadAllBlocks.clicked.connect(self.on_pb_ReadAllBlocks)
        self.ui.pb_ClearCard.clicked.connect(self.on_pb_ClearCard)

        # QtWidgets.QWidget.setTabOrder(self.ui.cob_Com, self.ui.pb_OpenOrClose)
        # QtWidgets.QWidget.setTabOrder(
        #     self.ui.pb_OpenOrClose, self.ui.chk_HexRecv)
        # QtWidgets.QWidget.setTabOrder(
        #     self.ui.chk_HexRecv, self.ui.pb_ClearRecv)
        # QtWidgets.QWidget.setTabOrder(
        #     self.ui.pb_ClearRecv, self.ui.chk_HexSend)
        # QtWidgets.QWidget.setTabOrder(self.ui.chk_HexSend, self.ui.pb_Send)
        # QtWidgets.QWidget.setTabOrder(self.ui.pb_Send, self.ui.cob_Com)

        self.show()

    def Log(self, s, txrx=0):
        if txrx == 0:
            color = 'red'
        else:
            color = 'green'
        self.ui.te_Recv.append('[<font color="' + color + '">' + getNowStr(False, True) + '</font>] ' + str(s))

    def on_pb_OpenOrClose_Clicked(self):
        if not self.reader.IsOpen():
            self.reader = Reader(
                self.ui.cob_Com.currentText())
            try:
                self.reader.Open()
            except Exception as e:
                # print(e)
                self.showTip(e)
                # print('lbl_Tip = ' + self.ui.lbl_Tip.text())
            if self.reader.IsOpen():
                self.showComStatus()
        else:
            self.reader.Close()
            self.showComStatus()

    def on_cob_Com_CurrentIndexChanged(self, index):
        if self.reader.IsOpen():
            self.on_pb_OpenOrClose_Clicked()
            if not self.reader.IsOpen():
                self.on_pb_OpenOrClose_Clicked()

    def showComStatus(self):
        if self.reader.IsOpen():
            # print(dir(self.ser))
            self.ui.pb_OpenOrClose.setText(getTxt('closePort'))
            self.ui.lbl_Com.setPixmap(QtGui.QPixmap(":/ico/on.png"))
            self.ui.lbl_Status.setText(
                {True: 'ON', False: 'OFF'}[self.reader.IsOpen()])
        else:
            self.ui.pb_OpenOrClose.setText(getTxt('openPort'))
            self.ui.lbl_Com.setPixmap(QtGui.QPixmap(":/ico/off.png"))
            self.ui.lbl_Status.setText(
                {True: 'ON', False: 'OFF'}[self.reader.IsOpen()])

    def showTip(self, tip, duration_ms=3000):
        self.ui.lbl_Tip.setText(str(tip))
        self.timerTip.start(duration_ms)

    # def refresh_UI_Recv(self, b):
    #     if self.ui.chk_HexRecv.isChecked():
    #         s1 = func.buf2hexstr(b)
    #         s2 = '[<font color="red">' + \
    #             getNowStr(False, True) + '</font>] %04u: ' % len(b)
    #         s = s2 + s1
    #         self.ui.te_Recv.append(s)  # 换行追加
    #     else:
    #         s = bytes.decode(b, 'utf-8', errors='ignore')
    #         self.ui.te_Recv.moveCursor(QtGui.QTextCursor.End)
    #         self.ui.te_Recv.insertPlainText(s)

    # def on_pb_Send_Clicked(self):
    #     if self.ser.isOpen():
    #         txt = self.ui.te_Send.toPlainText()
    #         print('txt = ' + txt)
    #         for c in txt:
    #             if not c.upper() in ('%X' % x for x in range(0,16)):
    #                 self.ui.lbl_Tip.setText('Hex Data Format Err!')
    #                 self.timerTip.start(3000)
    #                 return
    #         if self.ui.chk_HexSend.isChecked():
    #             try:
    #                 b = func.hexstr2buf(txt)
    #             except Exception as e:
    #                 print(e)
    #                 self.ui.lbl_Tip.setText(str(e))
    #                 self.timerTip.start(3000)
    #                 return
    #         else:
    #             b = bytes(txt, 'utf-8')
    #         self.ser.write(b)

    def on_pb_ClearRecv_Clicked(self):
        self.ui.te_Recv.setText('')

    def timerTipProc(self):
        self.ui.lbl_Tip.setText('')

    def on_pb_Beep(self):
        self.Log('Beep')
        r = self.reader.DevBeep()
        self.Log(r, 1)

    def on_pb_Request(self):
        self.Log('Request')
        r = self.reader.Request()
        if r and func.IsSwOk(r[1]):
            self.ui.le_Atqa.setText(r[2])
        self.Log(r, 1)

    def on_pb_RequestAll(self):
        self.Log('RequestAll')
        r = self.reader.Request(1)
        if r and func.IsSwOk(r[1]):
            self.ui.le_Atqa.setText(r[2])
        self.Log(r, 1)

    def on_pb_Anticol(self):
        self.Log('Anticol')
        r = self.reader.Anticoll()
        if r and func.IsSwOk(r[1]):
            self.ui.le_Csn.setText(r[2])
        self.Log(r, 1)

    def on_pb_SelectCard(self):
        csn = self.ui.le_Csn.text()
        self.Log('SelectCard ' + csn)
        r = self.reader.SelectCard(csn)
        if r and func.IsSwOk(r[1]):
            self.ui.le_Sak.setText(r[2])
        self.Log(r, 1)

    def on_pb_FoundCard(self):
        self.Log('SelectCard')
        r = self.reader.FoundCard()
        if r and func.IsSwOk(r[1]):
            self.ui.le_Atqa.setText(r[2][0:4])
            self.ui.le_Sak.setText(r[2][4:6])
            self.ui.le_Csn.setText(r[2][6:])
        self.Log(r, 1)

    def on_pb_HaltCard(self):
        self.Log('HaltCard')
        r = self.reader.HaltCard()
        self.Log(r, 1)

    def on_pb_ReadBlock(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        blockno = int(blocknostr, 10)
        self.Log('ReadBlock ' + blocknostr)
        r = self.reader.ReadBlock(blockno)
        if r and func.IsSwOk(r[1]):
            self.ui.le_ReadBlock.setText(r[2])
        self.Log(r, 1)

    def on_pb_WriteBlock(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        blockno = int(blocknostr, 10)
        data = self.ui.le_WriteBlock.text()
        if len(data) != 32 or not func.ishexstr(data):
            # QMessageBox.information(self, 'Caution', 'Write block data fmt err!' + ' [' + data + ']', QMessageBox.Ok)
            self.showTip('Write block data fmt err!' + ' [' + data + ']')
            return
        if blockno in range(3, 64, 4):
            reply = QMessageBox.information(self, 'Caution', 'Sure to write key block?', QMessageBox.Yes | QMessageBox.No)
            if QMessageBox.No == reply:
                return
        self.Log('WriteBlock ' + blocknostr + ' ' + data)
        r = self.reader.WriteBlock(blockno, data)
        self.Log(r, 1)

    def on_pb_LoadKeyA(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        secno = int(blocknostr, 10) // 4
        key = self.ui.le_KeyA.text()
        self.Log('LoadKeyA %d ' % secno + key)
        r = self.reader.LoadKey(1, secno, key)
        self.Log(r, 1)

    def on_pb_LoadKeyB(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        secno = int(blocknostr, 10) // 4
        key = self.ui.le_KeyB.text()
        self.Log('LoadKeyB %d ' % secno + key)
        r = self.reader.LoadKey(4, secno, key)
        self.Log(r, 1)

    def on_pb_AuthKeyA(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        secno = int(blocknostr, 10) // 4
        self.Log('AuthKeyA %d' % secno)
        r = self.reader.AuthKey(1, secno)
        self.Log(r, 1)

    def on_pb_AuthKeyB(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        secno = int(blocknostr, 10) // 4
        self.Log('AuthKeyB %d' % secno)
        r = self.reader.AuthKey(4, secno)
        self.Log(r, 1)

    def on_pb_ReadValue(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        blockno = int(blocknostr, 10)
        self.Log('ReadVal ' + blocknostr)
        r = self.reader.ReadVal(blockno)
        if r and func.IsSwOk(r[1]):
            v = int(r[2], 16)
            self.ui.le_ReadValue.setText('%d (0x%s)' % (v, r[2]))
        self.Log(r, 1)

    def on_pb_WriteValue(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        blockno = int(blocknostr, 10)
        val = self.ui.le_WriteValue.text()
        try:
            val = int(val, 10)
        except Exception as e:
            self.showTip(e)
            return
        if blockno in range(3, 64, 4):
            # QMessageBox.information(self, 'Caution', 'Cannot write key block!', QMessageBox.Ok)
            self.showTip('Cannot write key block!')
            return
        self.Log('WriteVal %s %d' % (blocknostr, val))
        r = self.reader.WriteVal(blockno, val)
        self.Log(r, 1)

    def on_pb_IncValue(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        blockno = int(blocknostr, 10)
        val = self.ui.le_IncValue.text()
        try:
            val = int(val, 10)
        except Exception as e:
            self.showTip(e)
            return
        if blockno in range(3, 64, 4):
            # QMessageBox.information(self, 'Caution', 'Cannot inc key block!', QMessageBox.Ok)
            self.showTip('Cannot inc key block!')
            return
        self.Log('IncVal %s %d' % (blocknostr, val))
        r = self.reader.IncVal(blockno, val)
        self.Log(r, 1)

    def on_pb_DecValue(self):
        blocknostr = self.ui.cob_BlockNo.currentText()
        blockno = int(blocknostr, 10)
        val = self.ui.le_DecValue.text()
        try:
            val = int(val, 10)
        except Exception as e:
            self.showTip(e)
            return
        if blockno in range(3, 64, 4):
            # QMessageBox.information(self, 'Caution', 'Cannot dec key block!', QMessageBox.Ok)
            self.showTip('Cannot dec key block!')
            return
        self.Log('DecVal %s %d' % (blocknostr, val))
        r = self.reader.DecVal(blockno, val)
        self.Log(r, 1)

    def on_pb_Restore(self):
        blocknostr = self.ui.le_RestoreBlockNo.text()
        try:
            blockno = int(blocknostr, 10)
        except Exception as e:
            self.showTip(e)
            return
        if blockno in range(3, 64, 4):
            # QMessageBox.information(self, 'Caution', 'Cannot restore key block!', QMessageBox.Ok)
            self.showTip('Cannot restore key block!')
            return
        if blockno >= 64 or blockno < 0:
            self.showTip('Block No Err! [%s]' % blocknostr)
            return
        self.Log('Restore %d' % (blockno))
        r = self.reader.Restore(blockno)
        self.Log(r, 1)

    def on_pb_Transfer(self):
        blocknostr = self.ui.le_TransferBlockNo.text()
        try:
            blockno = int(blocknostr, 10)
        except Exception as e:
            self.showTip(e)
            return
        if blockno in range(3, 64, 4):
            # QMessageBox.information(self, 'Caution', 'Cannot restore key block!', QMessageBox.Ok)
            self.showTip('Cannot transfer key block!')
            return
        if blockno >= 64 or blockno < 0:
            self.showTip('Block No Err! [%s]' % blocknostr)
            return
        self.Log('Transfer %d' % (blockno))
        r = self.reader.Transfer(blockno)
        self.Log(r, 1)

    def on_pb_SelectChannel(self):
        channel_index = self.ui.cob_Channel.currentIndex()
        channel_str = self.ui.cob_Channel.currentText()
        self.Log('SelectChannel ' + channel_str)
        r = self.reader.SelectChannel(channel_index+1)
        self.Log(r, 1)

    def on_pb_SelectSamSlot(self):
        slot_index = self.ui.cob_SamSlot.currentIndex()
        slot_str = self.ui.cob_SamSlot.currentText()
        self.Log('SelectSamSlot ' + slot_str)
        r = self.reader.SelectSamSlot(slot_index+1)
        self.Log(r, 1)

    def on_pb_SelectSamBaudrate(self):
        baud_index = self.ui.cob_SamBaudrate.currentIndex()
        baud_str = self.ui.cob_SamBaudrate.currentText()
        self.Log('SelectSamBaudrate ' + baud_str)
        r = self.reader.SelectSamBaudrate(baud_index+1)
        self.Log(r, 1)

    def on_pb_CpuReset(self):
        self.Log('CpuReset')
        r = self.reader.CpuReset()
        if r and func.IsSwOk(r[1]):
            self.ui.le_CpuReset.setText(r[2])
        self.Log(r, 1)

    def on_pb_CpuDeselect(self):
        self.Log('Deselect')
        r = self.reader.Deselect()
        self.Log(r, 1)

    def on_pb_CosCmd(self):
        coscmd = self.ui.le_CosCmd.text()
        if not func.ishexstr(coscmd):
            self.showTip('COS cmd fmt err! [%s]' % coscmd)
            return
        self.Log('CpuCmd ' + coscmd)
        r = self.reader.CpuCmd(coscmd)
        if r:
            self.ui.le_CosRetCode.setText(r[1])
            if r[2]:
                self.ui.le_CosRetData.setText(r[2])
        self.Log(r, 1)

    def on_pb_ReadSid(self):
        self.Log('DevReadSID')
        r = self.reader.DevReadSID()
        if r and func.IsSwOk(r[1]):
            self.ui.le_ReadSid.setText(r[2])
        self.Log(r, 1)

    def on_pb_ReadLkt4210Info(self):
        self.Log('DevReadLKT4210Info')
        r = self.reader.DevReadLKT4210Info()
        if r and func.IsSwOk(r[1]):
            self.ui.le_ReadLkt4210Info.setText(r[2])
        self.Log(r, 1)

    def on_pb_RfReset(self):
        delayms_str = self.ui.le_RfResetMs.text()
        try:
            delayms = int(delayms_str, 10)
        except Exception as e:
            self.showTip(e)
            return
        self.Log('ResetRF ' + delayms_str)
        r = self.reader.ResetRF(delayms)
        self.Log(r, 1)

    def on_pb_CpuPps(self):
        sendpps = self.ui.le_CpuPpsSend.text()
        self.Log('CpuPPS ' + sendpps)
        r = self.reader.CpuPPS(sendpps)
        if r and func.IsSwOk(r[1]):
            self.ui.le_CpuPpsRecv.setText(r[2])
        self.Log(r, 1)

    def on_pb_CalcKeyBs(self):
        self.Log('Calc KeyBs:')
        k = calcCardKeyBs(self.reader)
        if k:
            for i in range(16):
                self.Log('%02d ----- %s' % (i, k[i].hex()), 1)
        else:
            self.Log(k, 1)

    def on_pb_ReadAllBlocks(self):
        self.Log('Read All Blocks:')
        k = calcCardKeyBs(self.reader)
        if not k:
            self.Log('Calc KeyBs err!', 1)
            return
        r = self.reader.FoundCard()
        if not r or not func.IsSwOk(r[1]):
            self.Log('FoundCard err!', 1)
            return
        for i in range(64):
            sec = i//4
            r = self.reader.LoadKey(4, sec, k[sec])
            if not r or not func.IsSwOk(r[1]):
                self.Log('LoadKey %d %d %s err!' % (4, sec, k[sec]), 1)
                return
            r = self.reader.AuthKey(4, sec)
            if not r or not func.IsSwOk(r[1]):
                self.Log('AuthKey %d %d err!' % (4, sec), 1)
                return
            r = self.reader.ReadBlock(i)
            if not r or not func.IsSwOk(r[1]):
                self.Log('ReadBlock %d err!' % i, 1)
                return
            self.Log('%02d --- %s' % (i, r[2]), 1)

    def on_pb_ClearCard(self):
        reply = QMessageBox.information(self, 'Caution', 'Sure to clear card?', QMessageBox.Yes | QMessageBox.No)
        if QMessageBox.No == reply:
            return
        self.Log('Clear Card:')
        blockdata = 'FFFFFFFFFFFFFF078069FFFFFFFFFFFF'
        k = calcCardKeyBs(self.reader)
        if not k:
            self.Log('Calc KeyBs err!', 1)
            return
        r = self.reader.FoundCard()
        if not r or not func.IsSwOk(r[1]):
            self.Log('FoundCard err!', 1)
            return
        for i in range(3, 64, 4):
            sec = i//4
            r = self.reader.LoadKey(4, sec, k[sec])
            if not r or not func.IsSwOk(r[1]):
                self.Log('LoadKey %d %d %s err!' % (4, sec, k[sec]), 1)
                return
            while True:
                r = self.reader.AuthKey(4, sec)
                if not r or not func.IsSwOk(r[1]):
                    self.Log('AuthKey %d %d err!' % (4, sec), 1)
                    reply = QMessageBox.information(self, 'Caution', 'Yes to continue, No to Exit!', QMessageBox.Yes | QMessageBox.No)
                    if QMessageBox.No == reply:
                        return
                    else:
                        self.reader.FoundCard()
                        continue
                r = self.reader.WriteBlock(i, blockdata)
                if not r or not func.IsSwOk(r[1]):
                    self.Log('WriteBlock %d %s err!' % (i, blockdata), 1)
                    reply = QMessageBox.information(self, 'Caution', 'Yes to continue, No to Exit!', QMessageBox.Yes | QMessageBox.No)
                    if QMessageBox.No == reply:
                        return
                    else:
                        self.reader.FoundCard()
                        continue
                break
            self.Log('Wr%02d --- %s' % (i, blockdata), 1)

    # def eventFilter(self, obj, ev):
    #     print('eventFilter')

    def keyPressEvent(self, ev):
        # print('keyPressEvent, ev = ' + str(ev.modifiers()) + ', ' + hex(ev.key()))
        if ev.key() == Qt.Key_Return:
            # print('Enter Key')
            # if ev.modifiers() == Qt.ControlModifier:
            #     # print('Ctrl Key')
            #     if QtWidgets.QWidget.focusWidget(self) == self.ui.te_Send:
            #         self.on_pb_Send_Clicked()
            # # else:
            # #     curWidg = QtWidgets.QWidget.focusWidget(self)
            if QtWidgets.QWidget.focusWidget(self) == self.ui.le_CosCmd:
                self.on_pb_CosCmd()

    def closeEvent(self, ev):
        if self.reader.IsOpen():
            self.reader.Close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
