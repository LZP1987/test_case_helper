#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:handle_cmd.py
@time:2020/08/12
"""

import re


class handle_cmd:
    def __init__(self):
        self.testCmd = {
            "OPEN_LCD_TEST": "OK",
            "GET_LCD_TEST_RESULT": "OK",
            "CLOSE_LCD_TEST": "OK",
            "OPEN_LED_TEST": "FAIL",
            "GET_LED_TEST_RESULT": "FAIL",
            "CLOSE_LED_TEST": "FAIL"
        }

    def execCmd(self, cmd):
        for item in self.testCmd.keys():
            if cmd == item:
                return self.testCmd[item]
        return None


if __name__ == '__main__':
    cmds = handle_cmd()
    for item in cmds.testCmd.keys():
        print(item, cmds.testCmd[item])
        ret = cmds.execCmd(item)
        print('ret = {}'.format(ret))

