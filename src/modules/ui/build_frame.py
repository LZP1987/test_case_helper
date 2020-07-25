#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:build_frame.py
@time:2020/07/25
"""

from tkinter import *
import tkinter.ttk as ttk


def callbackFunction():
    print('callBack run!')


class build_frame:

    def __init__(self, frameX, frameY):
        self.btnX = 50
        self.btnY = 10
        self.frameX = frameX
        self.frameY = frameY

    def __addTextview(self, root):
        # print(self.root.grid_size())
        text = Text(root, width=50, height=40)  # 显示文本框
        text.place(x=10, y=100)

    def __addButton(self, root, btnName, callBack):
        button = Button(root, text=btnName, width=5, command=callBack)
        button.place(x=self.btnX, y=self.btnY)
        self.btnX = self.btnX + 50

    def buildFrame(self, root, frameName):
        self.btnX = 50
        self.btnY = 10
        tab = Frame(root)  # 创建一页框架
        tab.place(x=self.frameX, y=self.frameY)
        root.add(tab, text=frameName)  # 将第一页插入分页栏中
        self.frameX = self.frameX + 100
        # add button
        self.__addButton(tab, 'start', callbackFunction)
        self.__addButton(tab, 'stop', callbackFunction)
        # add textview
        self.__addTextview(tab)


if __name__ == '__main__':
    root = Tk()
    root.title('Test Case Helper')
    root.geometry('1600x1000+5+5')

    tab_main = ttk.Notebook()  # 创建分页栏
    tab_main.place(relx=0.02, rely=0.02, relwidth=0.887, relheight=0.876)

    tabx = build_frame(0, 30)
    tabx.buildFrame(tab_main, 'worker1')
    root.mainloop()
