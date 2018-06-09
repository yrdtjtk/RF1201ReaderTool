# -*- coding:utf-8 -*-
import sys

import time

import serial
import serial.tools.list_ports

import func

def createSerial(portName, baudrate):
    ser = serial.Serial()
    ser.port = portName
    ser.baudrate = baudrate
    ser.timeout = 2
    ser.parity = 'N'
    ser.stopbits = 1

    return ser


class Reader(object):
    """docstring for Reader"""

    def __init__(self, port):
        super(Reader, self).__init__()
        self.ser = createSerial(port, 57600)

    @staticmethod
    def GetInputBytes(*data):
        if data == None:
            return bytes()
        baData = bytes()
        for d in data:
            if d == None:
                pass
            elif isinstance(d, int):
                baData += bytes(chr(d), 'ISO8859-1')
            elif isinstance(d, bytes):
                baData += d
            elif isinstance(d, str):
                if func.ishexstr(d):
                    baData += func.hexstr2buf(d)
                else:
                    raise Exception('data format err!')
            else:
                raise Exception('data format err! curr type of data is ' + str(type(d)) + '.')
        return baData

    @staticmethod
    def Pack(cmd, *data):
        if isinstance(cmd, int):
            iCmd = cmd
        elif isinstance(cmd, bytes):
            if len(cmd) == 1:
                iCmd = cmd[0]
            else:
                raise Exception('If cmd is bytes, its len must be one!')
        elif isinstance(cmd, str):
            if len(cmd) == 2 and func.ishexstr(cmd):
                iCmd = func.hexstr2buf(cmd)[0]
            else:
                raise Exception('cmd format err!')
        else:
            raise Exception('cmd format err!')

        baData = Reader.GetInputBytes(*data)

        datalen = len(baData)
        ba = bytearray(datalen + 5)
        ba[0] = 0xAA
        ba[1] = datalen + 2
        ba[2] = iCmd
        for i in range(datalen):
            ba[3+i] = baData[i]
        ba[3+datalen] = func.bcc(bytes(ba[1:3+datalen]))
        ba[4+datalen] = 0xCC
        return func.buf2hexstr(ba)

    def Open(self):
        if not self.ser.isOpen():
            try:
                self.ser.open()
            except Exception as e:
                # print(e)
                raise e
        if self.ser.isOpen():
            return True
        else:
            return False

    def Close(self):
        if self.ser.isOpen():
            try:
                self.ser.close()
            except Exception as e:
                print(e)
        if self.ser.isOpen():
            return False
        else:
            return True

    def IsOpen(self):
        return self.ser.isOpen()

    def Transceive(self, cmd, *data, timeout=3.0):
        if self.ser.isOpen():
            sSend = self.Pack(cmd, *data)
            sCmd = sSend[4:6]
            self.ser.write(bytes(sSend, 'utf-8'))
            t1 = time.time()
            ba = bytes()
            while time.time() - t1 <= timeout:
                if self.ser.inWaiting():
                    ba += self.ser.read(self.ser.inWaiting())
                    # print(ba)
                    if len(ba) >= 4:
                        if ba.startswith(b'BB'):
                            rlen = 0
                            try:
                                rlen = func.hexstr2buf(ba[2:4])[0]
                                # print('rlen = ' + str(rlen))
                            except Exception as e:
                                print(e)
                                ba = bytes()
                                time.sleep(0.01)
                                continue
                            if len(ba) >= (rlen+3)*2:
                                if ba.endswith(b'CC'):
                                    if str(ba[4:6], 'utf-8') != sCmd:
                                        return (False, None, None)
                                    sRecv = str(ba[2:-2], 'utf-8')
                                    try:
                                        baRecv = func.hexstr2buf(sRecv)
                                        if func.bcc(baRecv[0:-1]) == baRecv[-1]:
                                            retcode = sRecv[4:8]
                                            retdata = sRecv[8:-2]
                                            return (True, retcode, retdata)
                                        else:
                                            return (False, None, None)
                                    except Exception as e:
                                        print(e)
                                        ba = bytes()
                                        time.sleep(0.01)
                                        continue
                                else:
                                    ba = bytes()
                                    time.sleep(0.01)
                                    continue
                        else:
                            ba = bytes()
                            time.sleep(0.01)
                            continue
        else:
            return (False, None, None)

    def DevReadSID(self):
        return self.Transceive(0x20)

    def DevReset(self):
        return self.Transceive(0x21)

    def DevReadStatus(self):
        return self.Transceive(0x22)

    '''channel:01-非接触式卡 02-接触式CPU卡 03-接触式PSAM卡'''
    def SelectChannel(self, channel):
        return self.Transceive(0x23, channel)

    '''slot: 01-1号插座 02-2号插座 03-3号插座 04-4号插座'''
    def SelectSamSlot(self, slot):
        return self.Transceive(0x24, slot)

    '''baud:01-9600（操作低速isam卡） 02-38400（操作高速psam卡） 03-19200 04-56000 05-115200'''
    def SelectSamBaudrate(self, baud):
        return self.Transceive(0x25, baud)

    '''delayms:掉电后等待多长时间后重新上电，单位毫秒'''
    def ResetRF(self, delayms=1):
        return self.Transceive(0x26, delayms)

    '''返回19字节LKT4210型RSA安全芯片卡的基本信息'''
    def DevReadLKT4210Info(self):
        return self.Transceive(0x27)

    '''mode: 00 -IDLE 01 -- ALL'''
    '''返回2字节的ATQ'''
    def Request(self, mode=0):
        return self.Transceive(0x30, mode)

    '''mode: 00 -IDLE 01 -- ALL'''
    '''返回4(7或10)字节卡芯片号'''
    def Anticoll(self, mode=0):
        return self.Transceive(0x31, mode)

    '''csn: 要选择的卡芯片号'''
    '''返回4(7或10)字节卡芯片号'''
    def SelectCard(self, csn):
        return self.Transceive(0x32, csn)

    '''mode: 00 -IDLE 01 -- ALL'''
    '''返回 ATQ(2B) + SAK(1B) + CSN(4/7/10B))'''
    def FoundCard(self, mode=0):
        return self.Transceive(0x35, mode)

    def DevBeep(self):
        return self.Transceive(0x33)

    def HaltCard(self):
        return self.Transceive(0x34)

    '''返回复位信息字节'''
    def CpuReset(self):
        return self.Transceive(0x40)

    def Deselect(self):
        return self.Transceive(0x41)

    def CpuCmd(self, sendcos):
        return self.Transceive(0x42, sendcos)

    def CpuPPS(self, sendpps):
        return self.Transceive(0x43, sendpps)

    ''' mode: 01-消费密钥，04-充值密钥
        secno: 扇区号
        key: 6字节密钥
    '''
    def LoadKey(self, mode, secno, key):
        return self.Transceive(0x50, mode, secno, key)

    ''' mode: 01-消费密钥，04-充值密钥
        secno: 扇区号
    '''
    def AuthKey(self, mode, secno):
        return self.Transceive(0x51, mode, secno)

    def ReadBlock(self, blockno):
        return self.Transceive(0x52, blockno)

    def WriteBlock(self, blockno, data):
        return self.Transceive(0x53, blockno, data)

    def ReadVal(self, blockno):
        return self.Transceive(0x54, blockno)

    def WriteVal(self, blockno, val):
        v = val
        if isinstance(v, int):
            v = '%08X' % v
        return self.Transceive(0x55, blockno, v)

    def IncVal(self, blockno, val):
        v = val
        if isinstance(v, int):
            v = '%08X' % v
        return self.Transceive(0x56, blockno, v)

    def DecVal(self, blockno, val):
        v = val
        if isinstance(v, int):
            v = '%08X' % v
        return self.Transceive(0x57, blockno, v)

    def Restore(self, blockno):
        return self.Transceive(0x58, blockno)

    def Transfer(self, blockno):
        return self.Transceive(0x59, blockno)


if __name__ == '__main__':
    # print(Reader.Pack(0x33, b'112233'))

    r = Reader('COM8')
    o = r.Open()
    print('Reader Open = ' + str(o))
    t = r.Transceive(0x27)
    print('Transceive = ' + str(t))
    print(r.FoundCard())
    r.DevBeep()
    print(r.LoadKey(1, 0, 'A0A1A2A3A4A5'))
    r.DevBeep()
    c = r.Close()
    print('Reader Close = ' + str(c))

    print(func.buf2hexstr(Reader.GetInputBytes(0x31, b'\x11\x22\x33', 'aabbccdd', 0x88, 0x99, 0xff, 0xee)))
