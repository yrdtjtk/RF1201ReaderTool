# -*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer, QThread
from ui_cpu_consume import Ui_Dialog
from PyQt5.QtWidgets import QMessageBox

import time
import datetime

from reader import Reader
import serial.tools.list_ports

import threading

import func
from res import images_qr

from crypt import *


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

def isApduRspOK(r):
    if r and func.IsSwOk(r[1]):
        return True
    else:
        return False


class ThreadCpuConsume(QThread):
    signalLog = QtCore.pyqtSignal(str, int)
    signalEnableConsumeButton = QtCore.pyqtSignal()
    
    def __init__(self, reader):
        super().__init__()
        self.reader = reader

    def __del__(self):
        self.wait()

    def Log(self, sLog, tx_or_rx = 0):
        self.signalLog.emit(str(sLog), tx_or_rx)

    def beep(self):
        self.Log('Beep')
        r = self.reader.DevBeep()
        self.Log(r, 1)
        return r

    def foundCard(self):
        self.Log('SelectCard')
        r = self.reader.FoundCard()
        # if r and func.IsSwOk(r[1]):
        #     self.ui.le_Atqa.setText(r[2][0:4])
        #     self.ui.le_Sak.setText(r[2][4:6])
        #     self.ui.le_Csn.setText(r[2][6:])
        self.Log(r, 1)
        return r

    def haltCard(self):
        self.Log('HaltCard')
        r = self.reader.HaltCard()
        self.Log(r, 1)
        return r


    def selectChannel(self, channel):
        self.Log('SelectChannel ' + str(channel))
        r = self.reader.SelectChannel(channel)
        self.Log(r, 1)
        return r

    def selectSamSlot(self, slot):
        self.Log('SelectSamSlot ' + str(slot))
        r = self.reader.SelectSamSlot(slot)
        self.Log(r, 1)
        return r

    def selectSamBaudrate(self, baud):
        self.Log('SelectSamBaudrate ' + str(baud))
        r = self.reader.SelectSamBaudrate(baud)
        self.Log(r, 1)
        return r

    def cpuReset(self):
        self.Log('CpuReset')
        r = self.reader.CpuReset()
        # if r and func.IsSwOk(r[1]):
        #     self.ui.le_CpuReset.setText(r[2])
        self.Log(r, 1)
        return r

    def cpuDeselect(self):
        self.Log('Deselect')
        r = self.reader.Deselect()
        self.Log(r, 1)
        return r

    def cosCmd(self, coscmd):
        self.Log('CpuCmd ' + coscmd)
        if not func.ishexstr(coscmd):
            self.Log('COS cmd fmt err! [%s]' % coscmd)
            return (False, None, None)
        r = self.reader.CpuCmd(coscmd)
        # if r:
        #     self.ui.le_CosRetCode.setText(r[1])
        #     if r[2]:
        #         self.ui.le_CosRetData.setText(r[2])
        self.Log(r, 1)
        return r

    def readSid(self):
        self.Log('DevReadSID')
        r = self.reader.DevReadSID()
        # if r and func.IsSwOk(r[1]):
        #     self.ui.le_ReadSid.setText(r[2])
        self.Log(r, 1)
        return r

    def rfReset(self, delayms):
        self.Log('ResetRF ' + str(delayms))
        r = self.reader.ResetRF(delayms)
        self.Log(r, 1)
        return r

    def cpuPps(self, sendpps):
        self.Log('CpuPPS ' + sendpps)
        r = self.reader.CpuPPS(sendpps)
        # if r and func.IsSwOk(r[1]):
        #     self.ui.le_CpuPpsRecv.setText(r[2])
        self.Log(r, 1)
        return r

    def consumeProc(self):
        self.Log('=============================CPU Consume Start===============================')
        isCapp = True #是否为复合交易 True是 False否
        r = self.beep()
        if not isApduRspOK(r):
            return
        r = self.rfReset(1)
        if not isApduRspOK(r):
            return
        r = self.foundCard()
        if not isApduRspOK(r):
            return
        r = self.selectChannel(1) #select contactless cpu card ----------------------
        if not isApduRspOK(r):
            return
        r = self.cpuReset()
        if not isApduRspOK(r):
            return
        r = self.cosCmd('00a4040009A00000000386980701') #select zjb cpu 3f01
        if not isApduRspOK(r):
            return
        r = self.cosCmd('00b0950000') #read zjb cpu 3f01 15
        if not isApduRspOK(r):
            return
        
        sCityNo = r[2][4:8]
        sCardAppSerial = r[2][24:40]
        self.Log("城市代码:" + sCityNo + " 卡应用序列号:" + sCardAppSerial)

        self.Log('------------------------last consume trade details---------------------------')
        self.Log('---seq-------overdraft-------amt-------type-------terminal----------date----------')
        for i in range(10):
            sNo = hex(i + 1)[2:]
            if len(sNo) < 2:
                sNo = '0' + sNo;
            r = self.cosCmd('00b2' + sNo + 'c400') #read zjb cpu 3f01 18 (last consume trade details)
            if not isApduRspOK(r):
                if r and r[0]:
                    break
                else:
                    return
            self.Log('   %s   %s    %s    %s     %s    %s' % (r[2][0:4], r[2][4:10], r[2][10:18], r[2][18:20], r[2][20:32], r[2][32:46]))

        self.Log('------------------------last recharge trade details---------------------------')
        self.Log('---seq-------overdraft-------amt-------type-------terminal----------date----------')
        for i in range(10):
            sNo = hex(i + 1)[2:]
            if len(sNo) < 2:
                sNo = '0' + sNo;
            r = self.cosCmd('00b2' + sNo + 'd400') #read zjb cpu 3f01 1a (last recharge trade details)
            if not isApduRspOK(r):
                if r and r[0]:
                    break
                else:
                    return
            self.Log('   %s   %s    %s    %s     %s    %s' % (r[2][0:4], r[2][4:10], r[2][10:18], r[2][18:20], r[2][20:32], r[2][32:46]))

        self.Log('------------------------capp proc record tag09---------------------------')
        r = self.cosCmd('00b209b800') #read zjb cpu 3f01 17 rec09 (capp proc record)
        if not isApduRspOK(r):
            return
        r = self.cosCmd('80ca000009') #read zjb cpu secure auth id
        if not isApduRspOK(r):
            return

        sSecureAuthID = r[2]
        self.Log("安全认证识别码:" + sSecureAuthID)

        r = self.selectChannel(3) #select SAM cpu card =============================
        if not isApduRspOK(r):
            return
        r = self.selectSamSlot(2) #select SAM Slot
        if not isApduRspOK(r):
            return
        r = self.selectSamBaudrate(2) #select cpu communicating baudrate, 1 - 9600, 2 - 38400
        if not isApduRspOK(r):
            return
        r = self.cpuReset()
        if not isApduRspOK(r):
            return
        r = self.cosCmd('00b0960006') #read zjb PSAM Terminal No 6 bytes
        if not isApduRspOK(r):
            return

        sPsamNo = r[2]
        self.Log("PSAM终端编号:" + sPsamNo)

        r = self.cosCmd('00a4040006BDA8C9E8B2BF') #select zjb PSAM purse application
        if not isApduRspOK(r):
            return
        r = self.cosCmd('00b0970001') #read zjb PSAM KeyIndex 1 byte
        if not isApduRspOK(r):
            return

        sKeyIndex = r[2]
        self.Log("PSAM密钥索引号:" + sKeyIndex)

        r = self.cosCmd('80ca000009' + sSecureAuthID) #PSAM verify zjb user card's secure auth id
        if not isApduRspOK(r):
            return
            
        r = self.selectChannel(1) #select contactless cpu card ----------------------------
        if not isApduRspOK(r):
            return

        if isCapp:
            P1 = '03'
            sTradeType = '09'
        else:
            P1 = '01'
            sTradeType = '06'
        sSubAmt = '00000001'
        self.Log("消费金额:" + sSubAmt)
        r = self.cosCmd('8050' + P1 + '020b' + sKeyIndex + sSubAmt + sPsamNo) #8050 init for purchase
        if not isApduRspOK(r):
            return
        # return #############################################################################################
        sBalance = r[2][:8]
        sIccTradeSeq = r[2][8:12]
        sOverdraft = r[2][12:18]
        sKeyVer = r[2][18:20]
        sAlgID = r[2][20:22]
        sRandom = r[2][22:30]
        self.Log("余额:" + sBalance + " 脱机交易序号:" + sIccTradeSeq + " 透支限额:" + sOverdraft + " 密钥版本号:" + sKeyVer + " 算法标识:" + sAlgID + " 伪随机数:" + sRandom)

        r = self.selectChannel(3) #select SAM cpu card =============================
        if not isApduRspOK(r):
            return
        sNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        r = self.cosCmd('8070000024' + sRandom + sIccTradeSeq + sSubAmt + sTradeType + sNow + sKeyVer + sAlgID + sCardAppSerial + sCityNo + 'FF0000000000') #8070 init SAM for purchase
        if not isApduRspOK(r):
            return
        
        sPsamTradeSeq = r[2][:8]
        sMAC1 = r[2][8:16]
        self.Log("终端脱机交易序号:" + sPsamTradeSeq + " MAC1:" + sMAC1)

        r = self.selectChannel(1) #select contactless cpu card ----------------------------
        if not isApduRspOK(r):
            return
        if isCapp:
            self.Log('------------------------update capp proc record tag09---------------------------')
            r = self.cosCmd('80dc09b830092E00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011') #update zjb cpu 3f01 17 rec09 (capp proc record)
            if not isApduRspOK(r):
                return

        r = self.cosCmd('805401000f' + sPsamTradeSeq + sNow + sMAC1) #8054 debit for purchase
        if not isApduRspOK(r):
            return
        sTAC = r[2][:8]
        sMAC2 = r[2][8:16]
        self.Log("TAC:" + sTAC + " MAC2:" + sMAC2)

        r = self.selectChannel(3) #select SAM cpu card =============================
        if not isApduRspOK(r):
            return
        r = self.cosCmd('8072000004' + sMAC2) #8072 debit SAM for purchase
        if not isApduRspOK(r):
            return


        self.Log('=============================CPU Consume End===============================')
        r = self.beep()
        if not isApduRspOK(r):
            return
        r = self.beep()
        if not isApduRspOK(r):
            return
        return
        
    def run(self):
        self.consumeProc()
        self.signalEnableConsumeButton.emit()


class DlgCpuConsume(QtWidgets.QDialog):

    def __init__(self, reader, parent=None):
        super(DlgCpuConsume, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.t = None


        self.setWindowTitle('RF1201 Card Reader Tool - ' + "CPU Consume")

        self.reader = reader

        self.ui.pb_Consume.clicked.connect(self.on_pb_Consume)
        self.ui.pb_ClearLog.clicked.connect(self.on_pb_ClearLog)

        self.show()
        # QMessageBox.information(self, 'Caution --', "sdfsdfsdfsd")

    def Log(self, s, txrx=0):
        if txrx == 0:
            color = 'red'
        else:
            color = 'green'
        self.ui.te_Log.append('[<font color="' + color + '">' + getNowStr(False, True) + '</font>] ' + str(s))

    def consumeButtonEnable(self):
        self.ui.pb_Consume.setEnabled(True)

    def on_pb_Consume(self):
        self.ui.pb_Consume.setEnabled(False)
        self.thd = ThreadCpuConsume(self.reader)
        self.thd.signalLog.connect(self.Log)
        self.thd.signalEnableConsumeButton.connect(self.consumeButtonEnable)
        self.thd.start()

    def on_pb_ClearLog(self):
        self.ui.te_Log.setText('');

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
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    reader = 1
    dlg = DlgCpuConsume(reader)
    sys.exit(app.exec_())








# import sys
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QLineEdit
# from PyQt5.QtCore import pyqtSignal

# """
# 自定义对话框
# """
# class MyDialog(QDialog):

#     # 自定义信号
#     mySignal = pyqtSignal(str)

#     def __init__(self, parent = None):
#         super(MyDialog, self).__init__(parent)
#         self.initUI()


#     def initUI(self):
#         self.edit = QLineEdit(self)
#         self.edit.move(10, 10)
#         button = QPushButton('发送', self)
#         button.move(10, 40)
#         button.clicked.connect(self.sendEditContent)
#         self.setWindowTitle('MyDialog')
#         self.setGeometry(300, 300, 300, 200)

#     def sendEditContent(self):
#         content = self.edit.text()
#         self.mySignal.emit(content) # 发射信号

# """
# 主窗口
# """
# class Window(QWidget):

#     def __init__(self):
#         super(Window, self).__init__()
#         self.initUI()

#     def initUI(self):
#         self.button = QPushButton('open', self)
#         self.button.clicked.connect(self.openMyDialog)
#         self.button.move(10, 10)
#         self.label = QLabel("hello", self)
#         self.label.move(10, 50)
#         self.setWindowTitle('Window')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()

#     def openMyDialog(self):
#         my = MyDialog(self)
#         # 在主窗口中连接信号和槽
#         my.mySignal.connect(self.getDialogSignal)
#         my.exec_()

#     """
#     实现槽函数
#     """
#     def getDialogSignal(self, connect):
#         self.label.setText(connect)


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)

#     reader = 1
#     mainwindow = Window()
#     sys.exit(app.exec_())
