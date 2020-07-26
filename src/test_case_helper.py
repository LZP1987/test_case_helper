#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:test_case_helper.py
@time:2020/07/24
"""

import modules.ui.build_ui


class test_case_helper:
    def __init__(self):
        print("test_case_helper init")

    def initUi(self):
        self.ui = modules.ui.build_ui.build_ui()
        self.ui.buildUi()
        self.ui.run()


if __name__ == '__main__':
    helper = test_case_helper()
    helper.initUi()
