#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:test_case_parser.py
@time:2020/07/24
"""

# from xml.dom.minidom import parse
import xml.dom.minidom


class at_cmd_data:
    def __init__(self, cmd, ret):
        self.cmd = cmd
        self.ret = ret

    def __str__(self):
        return ("cmd={},return={}".format(self.cmd, self.ret))


class test_case_data:
    def __init__(self, title):
        self.title = title
        self.cmdDatas = []
        # print("test_case_data init")

    def AddCmdData(self, cmdData):
        self.cmdDatas.append(cmdData)

    def __str__(self):
        return ("title={},cmdDatas={}".format(self.title, self.cmdDatas))


class test_case:
    def __init__(self):
        self.testCaseList = []

    def __parseCmdData(self, cmd):
        tempCmd = ""
        if cmd.hasAttribute("AT"):
            tempCmd = cmd.getAttribute("AT")
            print("cmd: AT=%s" % tempCmd)
        ret = cmd.getElementsByTagName('return')[0]
        tempRet = ret.childNodes[0].data
        print("return: %s" % tempRet)
        cmdData = at_cmd_data(tempCmd, tempRet)
        # print(cmdData)
        return cmdData

    # 使用minidom解析器打开 XML 文档
    def parse_test_case(self, file="../../data/input/test_case1.xml"):
        print("file=", file)
        DOMTree = xml.dom.minidom.parse(file)
        collection = DOMTree.documentElement
        if collection.hasAttribute("shelf"):
            print("Root element : %s" % collection.getAttribute("shelf"))

        # 在集合中获取所有case
        cases = collection.getElementsByTagName("case")

        # 获取每个case的详细信息
        for case in cases:
            print("*****cases*****")
            if case.hasAttribute("title"):
                print("Title: %s" % case.getAttribute("title"))
            caseData = test_case_data(case.getAttribute("title"))
            cmds = collection.getElementsByTagName("cmd")
            for cmd in cmds:
                cmdData = self.__parseCmdData(cmd)
                caseData.AddCmdData(cmdData)
            # print("caseData:",caseData)
            self.testCaseList.append(caseData)
            return self.testCaseList


if __name__ == '__main__':
    testCase = test_case()
    testCaseList = testCase.parse_test_case()
    testMovieList = testCase.parse_test_case(file="../../data/input/test_case2.xml")
