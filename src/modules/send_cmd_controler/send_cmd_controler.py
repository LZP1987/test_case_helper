#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:三哥
@email:516264135@qq.com
@file:send_cmd_controler.py
@time:2020/07/28
"""

import modules.xls.test_result_saving as TEST_RESULT
import modules.send_cmd_controler.socket.send_cmd_by_socket as SCBS
import modules.send_cmd_controler.serial.send_cmd_by_serial as SCBS2
import re

class send_cmd_controler:
    def __init__(self):
        print("send_cmd_controler init")
        self.senderType = 0

    def openSender(self):
        if self.senderType == 0:
            self.cmdHandle = SCBS.send_cmd_by_socket()
        else:
            self.cmdHandle = SCBS2.send_cmd_by_serial()
        return self.cmdHandle.openSender()

    def closeSender(self):
        self.cmdHandle.closeSender()  # 关闭客户端

    def __printCmdInfo(self, text, info):
        if not text:
            print('text is none')
        else:
            text.insert("end", '\n{}\n'.format(info))

    def __handleCmdResult(self, cmdRet, pattern):
        if not cmdRet:
            print('cmdRet is none')
            return None
        else:
            # pattern = oneCmd.cmd + oneCmd.ret
            return re.search(pattern, cmdRet, flags=0)

    def sendCmdList(self, caseList, text):
        caseResultList = []
        for case in caseList:
            print('case type=', type(case))
            testCaseResult = TEST_RESULT.test_case_result(case.title)
            print(testCaseResult)
            for oneCmd in case.cmdDatas:
                self.__printCmdInfo(text, 'TX:{}'.format(oneCmd.cmd))
                self.cmdHandle.sendData(oneCmd.cmd.encode('utf-8'))  # 发送消息
                ret = self.cmdHandle.receiveData()  # 读取消息
                if not ret:
                    break
                print(ret.decode('utf-8'))
                self.__printCmdInfo(text, 'RX:{}'.format(ret.decode('utf-8')))
                reRet = self.__handleCmdResult(ret.decode('utf-8'), oneCmd.ret)
                if not reRet:
                    cmdResult = TEST_RESULT.cmd_result(ret.decode('utf-8'), oneCmd.ret, 'fail')
                else:
                    cmdResult = TEST_RESULT.cmd_result(ret.decode('utf-8'), oneCmd.ret, 'pass')
                testCaseResult.addResult(cmdResult)
            caseResultList.append(testCaseResult)
        # save result to file
        saveResult = TEST_RESULT.test_result_saving('test12')
        saveResult.saveTestResult(caseResultList)

if __name__ == '__main__':
    pass
