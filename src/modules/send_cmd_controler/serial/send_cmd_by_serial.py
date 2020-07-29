#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:send_cmd_by_serial.py
@time:2020/07/24
"""

import serial  # 导入串口包
import serial.tools.list_ports
import time  # 导入时间包


class send_cmd_by_serial:
    def __init__(self):
        print("send_cmd_by_serial init")
        self.port = 'com1'
        self.bps = 115200
        self.timeOut = 5

    def openSender(self):
        self.plist = list(serial.tools.list_ports.comports())
        if self.port not in self.plist:
            print('the \'{}\' not found'.format(self.port))
            print('serial list:\n{}'.format(self.plist))
            return 'fail'
        self.ser = serial.Serial(self.port, self.bps, self.timeOut)
        if self.ser.isOpen():
            print("{} has been open!".format(self.port))
            return 'fail'
        self.ser.flushInput()  # 清空缓冲区
        return 'ok'
    def receiveData(self):
        count = self.ser.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            recv = self.ser.read(self.ser.in_waiting).decode("gbk")  # 读出串口数据，数据采用gbk编码
            print(time.time(), " ---  recv --> ", recv)  # 打印一下子
            return recv
        return None

    def sendData(self, data):
        self.ser.write(data)

    def closeSerial(self):
        self.ser.close()

    def __str__(self):
        return (self.ser)


if __name__ == '__main__':
    sendCmdSerial = send_cmd_by_serial()
    ret = sendCmdSerial.openSender()  # 开启com3口，波特率115200，超时5
    if ret == 'ok':
        sendCmdSerial.sendData('hello')
        rev = sendCmdSerial.receiveData()
        print('rev={}'.format(rev))
        sendCmdSerial.closeSerial()
