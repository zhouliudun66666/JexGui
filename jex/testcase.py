#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

import unittest
import requestget
import config
import common
import xlrd
import time
import requests
import re
import htmlreport
import db

class TestCase(unittest.TestCase):

    def test(self):

        db.DB().make_product()
        table = xlrd.open_workbook("interface.xlsx").sheets()[0]
        for i in range(table.nrows):
            try:
                rq = requestget.Request(i)
                if common.List0[7] == '1':
                    TestCaseNo = "TestCase" + str(i + 1) + ":"
                    print(TestCaseNo)
                    htmlreport.TestCaseNo.append(TestCaseNo)
                    time.sleep(0.5)
                    a = rq.make_re()
                    b = common.List0[3]
                    # c = b.split('\n')
                    # for m in c:
                    #     if m == common.Common().get_matchstr(a, m, 0):
                    #         print('PASS')
                    #         htmlreport.Result.append('PASS')
                    #     else:
                    #         print ('FALL')
                    #         htmlreport.Result.append('FALL')
                    if b == common.Common().get_matchstr(a, b, 0):
                        print('PASS')
                        htmlreport.Result.append('PASS')
                    else:
                        print('FAIL')
                        htmlreport.Result.append('FAIL')

                    if common.List0[4] != '':
                        m = common.List0[4]
                        n = m.split('\n')
                        common.globe_para = []
                        for i in n:
                            sava_str = common.Common().get_matchstr(common.response, i, 1)
                            common.globe_para.append(sava_str)
                    else:
                        common.globe_para = []

                    if common.List0[5] != '':
                        m0 = common.List0[5]
                        n0 = m0.split('\n')
                        common.globe_para0 = []
                        for i in n0:
                            sava_str = common.Common().get_matchstr(common.response, i, 1)
                            common.globe_para0.append(sava_str)
                        if common.List0[5].find('tokenName') >= 0:
                            if  'tokenName' not in requestget.Request.headers['Cookie']:
                                requestget.Request.headers['Cookie'] = requestget.Request.headers['Cookie'] + 'tokenName=' + common.globe_para0[0] + ';' + 'tokenValue=' + common.globe_para0[1] + ';'
                            elif 'tokenName' in requestget.Request.headers['Cookie']:
                                aa = re.compile('tokenName=(.+?);').search(requestget.Request.headers['Cookie']).group(1)
                                bb = requestget.Request.headers['Cookie'].replace(aa, common.globe_para0[0])
                                requestget.Request.headers['Cookie'] = bb
                                mm = re.compile('tokenValue=(.+?);').search(requestget.Request.headers['Cookie']).group(1)
                                nn = requestget.Request.headers['Cookie'].replace(mm, common.globe_para0[1])
                                requestget.Request.headers['Cookie'] = nn
                            if common.List0[5].find('authorization') >= 0:
                                requestget.Request.headers['Authorization'] = common.globe_para0[2]
                    else:
                        common.globe_para0 = []

                    if common.List0[6] != '':
                        if common.List0[6].find('SESSIONID') >= 0:
                            common.globe_para1 = []
                            sava_str1 = common.Common().get_matchstr(common.header_cookie, common.List0[6] , 1)
                            common.globe_para1.append(sava_str1)
                            cc = re.compile('SESSIONID=(.+?);').search(requestget.Request.headers['Cookie']).group(1)
                            dd = requestget.Request.headers['Cookie'].replace(cc, common.globe_para1[0])
                            requestget.Request.headers['Cookie'] = dd
                    else:
                        common.globe_para1 = []
            except Exception as ex:
                print(ex)
        common.List0 = []

        htmlreport.make_report()
        common.progress = 1


