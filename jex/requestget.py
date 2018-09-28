#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

import config
import requests
import unittest
import common
import xlrd
import re
import db
import testcase
import htmlreport

class Request:

    init_r = requests.get(url=config.PreHttp + 'mobile/config.json')
    c = str(init_r.headers['Set-Cookie'])
    acc_sid = re.compile('acc_sid=(.+?);').search(c).group(1)
    SESSIONID = re.compile('SESSIONID=(.+?);').search(c).group(1)


    headers = {
        'Connection': 'keep-alive',
        'phoneuuid': 'e924767e-4448-4a3a-8c14-097095c7b10a',
        'Cookie': 'acc_sid='+acc_sid+';SESSIONID='+SESSIONID+';path=/;HttpOnly;',
        'Host': '172.17.255.219:8080',
        'Authorization': '',
    }

    def __init__(self,n):
        self.List0 = []
        table = xlrd.open_workbook("interface.xlsx").sheets()[0]
        ncols = table.ncols
        for i in range(0, ncols):
            data = table.cell(n, i).value
            self.List0.append(data)
        common.List0 = self.List0

    def make_re(self):
        if self.List0[2] != '':
            if 'common.sql_sms' in self.List0[2]:
                common.sql_sms = db.DB().get_code_sms()
            if 'common.sql_productId_plan' in self.List0[2]:
                common.sql_productId_plan = db.DB().get_product_id(3, 1)
            if 'common.sql_productId_sporadic' in self.List0[2]:
                common.sql_productId_sporadic = db.DB().get_product_id(1, 1)
            if 'common.sql_productId_new' in self.List0[2]:
                common.sql_productId_new = db.DB().get_product_id(1, 2)
            if 'tokenName' in self.List0[2]:
                common.token = []
                rt = requests.get(url=config.PreHttp + 'mobile/user/getToken.json', headers=self.headers)
                tn = re.compile('"tokenName":"(.*?)",').search(rt.text).group(1)
                common.token.append(tn)
                tv = re.compile('"tokenValue":"(.*?)"},').search(rt.text).group(1)
                common.token.append(tv)
            if '$' in self.List0[2] or '(' in self.List0[2]:
                b = re.compile('&').split(self.List0[2])
                for i in range(len(b)):
                    if '($' in b[i]:
                        re_com = re.compile('\$(.*?)\$')
                        s = re_com.search(b[i]).group(1)
                        c = re.sub(r'\$(.+?)\$', eval(s), self.List0[2], 1)
                        en_globe = re.compile('\((.*?)\)').findall(c)
                        r = requests.get(url=config.PreHttp + 'mobile/getencrypt.json', params='plaintext=' + en_globe[0])
                        en_code = re.compile('"data":"(.*?)","message"').search(r.text).group(1)
                        g = '('+en_globe[0]+')'
                        self.List0[2] = c.replace(g, en_code)
                    elif '(' in b[i] and '$' not in b[i]:
                        en_globe1 = re.compile('\((.*?)\)').findall(b[i])
                        r1 = requests.get(url=config.PreHttp + 'mobile/getencrypt.json', params='plaintext=' + en_globe1[0])
                        en_code1 = re.compile('"data":"(.*?)","message"').search(r1.text).group(1)
                        g1 =  '('+en_globe1[0]+')'
                        self.List0[2] = self.List0[2].replace(g1, en_code1)
                    elif '$' in b[i] and '(' not in b[i]:
                        re_com = re.compile('\$(.*?)\$')
                        s1 = re_com.search(b[i]).group(1)
                        eval(s1)
                        c1 = re.sub(r'\$(.+?)\$', eval(s1), self.List0[2], 1)
                        self.List0[2] = c1
            self.List0[2] = dict([(e.split('=')[0], e.split('=')[1]) for e in self.List0[2].split('&')])
        htmlreport.Params.append(self.List0[2])
        htmlreport.Request.append(self.List0[0])
        if self.List0[1] == 'get':
            r = requests.get(url=config.PreHttp + self.List0[0], headers=self.headers, params=self.List0[2])
        elif self.List0[1] == 'post':
            r = requests.post(url=config.PreHttp + self.List0[0], headers=self.headers, data=self.List0[2])
        common.response = r.text
        if 'json'in self.List0[0]:
            htmlreport.Response.append(r.text)
        else:
            htmlreport.Response.append('')
        print (r.text)
        if 'Set-Cookie' in r.headers :
            common.header_cookie = r.headers['Set-Cookie']
        return r.text












