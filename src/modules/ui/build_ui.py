#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:build_ui.py
@time:2020/07/24
"""

from tkinter import *
import tkinter.ttk as ttk

if __name__ == '__main__':
    import build_frame as bf
else:
    import modules.ui.build_frame as bf


class build_ui:

    def __init__(self):
        self.root = Tk()
        self.root.title('Test Case Helper')
        self.root.geometry('1366x768+5+5')
        self.frameX = 0
        self.frameY = 30

    def __addFrame(self, root, frameName):
        tabx = bf.build_frame(root, self.frameX, self.frameY)
        tabx.buildFrame(root, frameName)
        self.frameX = self.frameX + 100

    def buildUi(self):
        tab_main = ttk.Notebook()  # 创建分页栏
        tab_main.place(relx=0.02, rely=0.02, relwidth=1.0 - 0.03, relheight=1.0 - 0.02)
        self.__addFrame(tab_main, 'worker1')
        self.__addFrame(tab_main, 'worker2')

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    ui = build_ui()
    ui.buildUi()
    ui.run()
