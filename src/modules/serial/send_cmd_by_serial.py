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

    def openSerial(self, port='COM3', bps=115200, timeOut=5):
        self.plist = list(serial.tools.list_ports.comports())
        if 'COM3' not in self.plist:
            print('the \'COM3\' not found')
            print('serial list:\n{}'.format(self.plist))
            return 'fail'
        self.ser = serial.Serial(port, bps, timeOut)
        if self.ser.isOpen():
            print("{} has been open!".format(port))
            return 'fail'
        self.ser.flushInput()  # 清空缓冲区
        return 'ok'

    def sendCmd(self):
        while True:
            count = self.ser.inWaiting()  # 获取串口缓冲区数据
            if count != 0:
                recv = self.ser.read(self.ser.in_waiting).decode("gbk")  # 读出串口数据，数据采用gbk编码
                print(time.time(), " ---  recv --> ", recv)  # 打印一下子
            time.sleep(0.1)  # 延时0.1秒，免得CPU出问题

    def closeSerial(self):
        self.ser.close()

    def __str__(self):
        return (self.ser)


if __name__ == '__main__':
    sendCmdSerial = send_cmd_by_serial()
    ret = sendCmdSerial.openSerial(port='COM3', bps=115200, timeOut=5)  # 开启com3口，波特率115200，超时5
    if ret == 'ok':
        sendCmdSerial.sendCmd()
        sendCmdSerial.closeSerial()
