#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:test_result_saving.py
@time:2020/07/24
"""

import xlwt


class cmd_result:
    def __init__(self, cmd, ret, flag):
        self.cmd = cmd
        self.ret = ret
        self.passFlag = flag

    def __str__(self):
        return ('cmd={},ret={},passFlag={}'.format(self.cmd, self.ret, self.passFlag))


class test_case_result:
    def __init__(self, title):
        self.title = title
        self.cmdRetList = []

    def addResult(self, cmdRet):
        self.cmdRetList.append(cmdRet)

    def __str__(self):
        return 'title={}'.format(self.title)


class test_result_saving:
    def __init__(self, testCaseName):
        self.fileName = '../../data/output/{}.xls'.format(testCaseName)
        self.sheetName = 'testresult_{}'.format(testCaseName)

    def saveTestResult(self, testResultList):
        # data_number = 100  # 数据的个数
        workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
        sheet1 = workbook.add_sheet("result")  # 新建sheet

        sheet1.col(0).width = 3333
        sheet1.col(1).width = 6333
        sheet1.col(2).width = 6333
        sheet1.col(3).width = 6333
        sheet1.col(4).width = 6333

        sheet1.write(0, 0, "Title")  # 第1行第1列数据
        sheet1.write(0, 1, "cmd")  # 第1行第2列数据
        sheet1.write(0, 2, "return")
        sheet1.write(0, 3, "pass/fail")
        sheet1.write(0, 4, "tips")

        romNum = 1;
        for ret in testResultList:
            sheet1.write(romNum, 0, ret.title)  # case title
            romNum = romNum + 1
            for cmdRet in ret.cmdRetList:
                sheet1.write(romNum, 1, cmdRet.cmd)  # 保存cmd结果
                sheet1.write(romNum, 2, cmdRet.ret)  # 保存cmd.ret结果
                sheet1.write(romNum, 3, cmdRet.passFlag)  # 保存cmd.passFlag结果
                romNum = romNum + 1
        workbook.save(r'{}'.format(self.fileName))  # 保存


if __name__ == '__main__':
    # creat a cmd result
    cmdResult1 = cmd_result('open_cmd', 'OK', 'pass')
    cmdResult2 = cmd_result('close_cmd', 'OK', 'fail')
    print(cmdResult1)
    # creat case result
    testCaseResult = test_case_result('case1')
    testCaseResult.addResult(cmdResult1)
    testCaseResult.addResult(cmdResult2)
    testCaseResult2 = test_case_result('case2')
    testCaseResult2.addResult(cmdResult2)
    testCaseResult2.addResult(cmdResult1)
    print(testCaseResult)
    # creat case result list
    caseResultList = []
    caseResultList.append(testCaseResult)
    caseResultList.append(testCaseResult2)

    # save result to file
    saveResult = test_result_saving('test2')
    saveResult.saveTestResult(caseResultList)
