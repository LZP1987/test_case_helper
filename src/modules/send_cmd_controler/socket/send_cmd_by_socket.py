#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:send_cmd_by_socket.py
@time:2020/07/24
"""

import socket
# from time import ctime
# import test_result_saving as TEST_RESULT
import modules.xls.test_result_saving as TEST_RESULT


class send_cmd_by_socket:
    def __init__(self):
        self.BUFSIZ = 1024
        print("send_cmd_by_socket init")

    def getHostIp(self):
        """
        查询本机ip地址
        :return:
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    def __connect(self, host, port):
        ADDR = (host, port)
        self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
        self.tcpCliSock.connect(ADDR)  # 连接服务器

    def openSender(self):
        ip = self.getHostIp()
        if not ip:
            return 'fail'
        print(ip)
        self.__connect(ip, 21566)
        return 'ok'

    def closeSender(self):
        self.tcpCliSock.close()  # 关闭客户端

    def sendData(self, data):
        self.tcpCliSock.send(data)  # 发送消息

    def receiveData(self):
        return self.tcpCliSock.recv(self.BUFSIZ)  # 读取消息

    def testSendCmd(self):
        while True:
            data = input('>>').strip()
            if not data:
                break
            self.sendData(data.encode('utf-8'))  # 发送消息
            ret = self.receiveData()  # 读取消息
            if not ret:
                break
            print(ret.decode('utf-8'))
        self.closeSender()  # 关闭客户端


if __name__ == '__main__':
    # 获取本机IP
    sendCmd = send_cmd_by_socket()
    ip = sendCmd.getHostIp()
    print(ip)
    sendCmd = send_cmd_by_socket()
    sendCmd.openSender()
    sendCmd.testSendCmd()
    # cmdList = ['OPEN_LED', 'GET_RESULT', 'CLOSE_LED']
    # sendCmd.sendCmdList(ip, 21566, cmdList, )

