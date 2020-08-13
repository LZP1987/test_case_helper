#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:build_frame.py
@time:2020/07/25
"""

import tkinter as TK
import tkinter.ttk as ttk
import modules.send_cmd_controler.send_cmd_controler as SEND_CONTROLER
import modules.xml.test_case_parser as CMD_PARSER
import os



class build_frame:
    def __init__(self, root, frameX, frameY):
        self.btnX = 5
        self.btnY = 10
        self.btnFont = ("隶书", 14)
        self.frameX = frameX
        self.frameY = frameY
        root.update()
        self.width = root.winfo_width()
        self.height = root.winfo_height()
        # print("当前窗口的宽度为{}x{}".format(self.width, self.height))

    def sendCmd(self):
        pwd = os.getcwd()
        print('>>>>>>>>pwd='.format(pwd))
        testCase = CMD_PARSER.test_case()
        testCaseList = testCase.parse_test_case(file='E:/python/data/input/test_case1.xml')
        sender = SEND_CONTROLER.send_cmd_controler()
        sender.openSender()
        sender.sendCmdList(testCaseList, self.receiveText)


    def callbackStart(self):
        # self.receiveText.insert("end", "\nPython.com!")
        self.receiveText.delete(0.0, TK.END)
        self.sendCmd()

    def clearReceive(self):
        self.receiveText.delete(0.0, TK.END)

    def __addReceiveTextview(self, root):
        # 滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
        self.receiveText = TK.Text(root, width=self.width - 4, height=34, font=("宋体", 14))  # 显示文本框
        self.receiveText.place(x=2, y=50)

        self.scroll = TK.Scrollbar(root)
        self.scroll.config(command=self.receiveText.yview())  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
        self.scroll.pack(side=TK.RIGHT, fill=TK.Y)  # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
        self.receiveText.config(yscrollcommand=self.scroll.set)  # 将滚动条关联到文本框
        self.receiveText.insert("insert", "Welcome!")

    def __addButton(self, root, btnName, callBack):
        button = TK.Button(root, text=btnName, font=self.btnFont, width=5, command=callBack)
        button.place(x=self.btnX, y=self.btnY)
        self.btnX = self.btnX + 100

    def buildFrame(self, root, frameName):
        root.update()
        print("当前窗口的宽度为", root.winfo_width())
        self.btnX = 5
        self.btnY = 10
        tab = TK.Frame(root)  # 创建一页框架
        tab.place(x=self.frameX, y=self.frameY)
        root.add(tab, text=frameName)  # 将一页插入分页栏中
        self.frameX = self.frameX + 100
        # add button
        self.__addButton(tab, 'start', self.callbackStart)
        self.__addButton(tab, 'stop', self.clearReceive)
        # add textview
        self.__addReceiveTextview(tab)



if __name__ == '__main__':
    root = TK.Tk()
    root.title('Test Case Helper')
    root.geometry('1366x768+2+2')

    tab_main = ttk.Notebook()  # 创建分页栏
    tab_main.place(relx=0.01, rely=0.02, relwidth=1.0 - 0.01, relheight=1.0 - 0.03)

    tabx = build_frame(tab_main, 0, 30)
    tabx.buildFrame(tab_main, 'worker1')

    root.mainloop()
