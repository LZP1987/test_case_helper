#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:send_cmd_by_socket.py
@time:2020/07/24
"""

import socket
from time import ctime


class send_cmd_by_socket:
    def __init__(self):
        print("send_cmd_by_socket init")

    def get_host_ip(self):
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

    def send_cmd_handle(self, host, port):
        HOST = host  # 服务端ip
        PORT = port  # 服务端端口号
        BUFSIZ = 1024
        ADDR = (HOST, PORT)
        tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
        tcpCliSock.connect(ADDR)  # 连接服务器
        while True:
            data = input('>>').strip()
            if not data:
                break
            tcpCliSock.send(data.encode('utf-8'))  # 发送消息
            data = tcpCliSock.recv(BUFSIZ)  # 读取消息
            if not data:
                break
            print(data.decode('utf-8'))
        tcpCliSock.close()  # 关闭客户端


if __name__ == '__main__':
    # 获取本机IP
    sendCmd = send_cmd_by_socket()
    ip = sendCmd.get_host_ip()
    print(ip)
    port = 21566
    sendCmd = send_cmd_by_socket()
    sendCmd.send_cmd_handle(ip, 21566)
