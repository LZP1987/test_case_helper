#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:example_socket.py
@time:2020/07/24
"""

from socket import *
import time
import handle_cmd

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def socket_server():
    # 获取本机IP
    ip = get_host_ip()
    print(ip)
    COD = 'utf-8'
    HOST = ip  # 主机ip
    PORT = 21566  # 软件端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    SIZE = 10
    tcpS = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
    tcpS.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 加入socket配置，重用ip和端口
    tcpS.bind(ADDR)  # 绑定ip端口号
    tcpS.listen(SIZE)  # 设置最大链接数
    cmdsHandle = handle_cmd.handle_cmd()
    while True:
        print("服务器启动，监听客户端链接")
        conn, addr = tcpS.accept()
        print("链接的客户端", addr)
        while True:
            try:
                data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
            except Exception:
                print("断开的客户端", addr)
                break
            print("客户端发送的内容:", data.decode(COD))
            if not data:
                break
            # msg = time.strftime("%Y-%m-%d %X")  # 获取结构化事件戳
            # msg1 = '[%s]:%s' % (msg, data.decode(COD))
            ret = cmdsHandle.execCmd(data.decode(COD))
            msg1 = '[%s]: %s' % (data.decode(COD), ret)
            print("回复客户端的内容:", msg1)
            # msg1 = data.decode(COD)
            conn.send(msg1.encode(COD))  # 发送消息给已链接客户端
        conn.close()  # 关闭客户端链接
    tcpS.closel()


if __name__ == '__main__':
    socket_server()
