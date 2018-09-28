#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import requests
# import config
# import re
# import common
# import hashlib
#
# import xlrd
# # List0 = ['home.json', 'get', '']
# #
# # def make_re():
# #     r = None
# #     if List0[1] == 'get':
# #         r = requests.get(url=config.PreHttp + List0[0], params=List0[2])
# #     elif List0[1] == 'post':
# #         r = requests.post(url=config.PreHttp + List0[0], data=List0[2])
# #     return r.text
# #
# # print(make_re())
#
#
# #
# # a_str = '{"data":{"beginnerProductList":[{"id":34,"productName":"银票计划2016111601","'
# #
# # re_com = re.compile('{"id":(.*?),"productName":"银票计划2016111601"')
# #
# # print(re_com.search(a_str).group(1))
#
# # table = xlrd.open_workbook("interface.xlsx").sheets()[0]
# # nrows = table.nrows
# # ncols = table.ncols
# # print(ncols)
# # for i in range(ncols):
# #     data = table.cell(0, i).value
# #     print(data)
# #
# # a_str = 'cardNo=$common.Common().make_card("建设银行")$&aaa'
# # print(a_str.find("\$"))
# # if a_str.find("\$") is True:
# #     re_com = re.compile('\$(.*?)\$')
# #     s = re_com.search(a_str).group(1)
# #     gv = eval(s)
# #     print(gv)
# #     nn = re.sub(r'\$(.*?)\$', gv, a_str)
# #     print(nn)
# #     print(type(nn))
# #     print(a_str)
# # else:
# #     print('aaa')
#
#
# # a = '"message":"success"\n"code":"1"'
# # b = a.split('\n')
# # print(b)
# # for i in b:
# #     print(i)
# #
# # str0 = '{"data":{"staticUrl":"http://192.168.1.146:8080/c_1.1/","couponAmount":999,"noviceCount":1,"currentSign":"灵活理财，按日计息"},"message":"操作成功","code":"1","serviceDate":1480643707433}'
# # str1 = '"message":"操作成功"'
# # re_com = re.compile(str1)
# # matchstr = re_com.search(str0).group()
# # print(matchstr)
#
# # x = 'productId=$common.globe_para$aaa'
# # if x.find("\$") is True:
# #     print("aaa")
# # else:
# #     print("bbb")
#
#
# # a_str = 'cardNo=$common&aaa'
# # # print (a_str.find("$"))
# # if '$' in a_str:
# #     print ("aaa")
#
# # def md5(origin_str):
# #     m = hashlib.md5()
# #     m.update(origin_str.encode("utf8"))
# #     return m.hexdigest()
# #
# # print(md5("aaa12345"))
# #
# #
# # headers = {
# #     'a': '1',
# #     'b': '2'
# #            }
# #
# # list1= ['a','b']
# #
# # for i in list1:
# #     headers[i] = headers[i]+'0'
# #
# # print(headers)
# # a = 'mobile=$common.teleNum$&mobileCode=$common.sql$&origin=IOS100&password=$common.globe_para[0]$'
# # b = re.compile('&').split(a)
# # print(b)
# # re_com = re.compile('\$(.+)\$')
# # for i in range(len(b)):
# #     if '$' in b[i]:
# #         s = re_com.search(b[i]).group(1)
# #         print(s)
# #         c = re.sub(r'\$(.+?)\$', s, a, 1)
# #         a = c
# # print (a)
#
#
# # import requests
# # url = 'http://172.17.255.219/mobile/home.json'
# # # payload = {'key1': 'value1', 'key2': 'value2'}
# # payload = 'key1=value1&key2=value2'
# # r = requests.post(url, data=payload)
# # print (r.text)
# import json
# import urllib
# # a = 'mobile=aaa&mobileCode=bbb&origin=ccc&res=ddd'
# # a = {
# #      'mobile': 'aaa',
# #      'mobileCode': 'bbb',
# #      'origin': 'ccc'
# #      }
# # b = a.replace('=',':')
# # c = b.replace('&',',')
# # c = dict([(e.split('=')[0], e.split('=')[1]) for e in a.split('&')])
# # c = dict(urllib.parse(a))
# # print (c)
# # print (type(c))
# # c = re.compile('&').split(b)
# import requests
# import config
# r = requests.get(url=config.PreHttp + 'config.json')
# # m = str(r.headers['Set-Cookie'])
# print (type(r.headers))
# b = r.headers['Set-Cookie']
# print(b)
# c = {'a':'b'}
# print (type(c))


# # n = dict([(e.split('=')[0], e.split('=')[1]) for e in m.split(';')])
# acc_sid=re.compile('acc_sid=(.+?);').search(m).group(1)
# SESSIONID=re.compile('SESSIONID=(.+?);').search(m).group(1)
# print(acc_sid)
# # print(SESSIONID)
# import requests
# import config
# # a = 'bankCardNo=(aaa12345)&origin=IOS&idCardNo=($config.idCardNo$)&realName=民投君'
# # a = 'mobile=($common.teleNum$)'
# # a = 'currentVersion=140'
# # a='(a1234567)&confirmPassword=(a1234567)'
# # if '(' in a or '$' in a:
# #     b = re.compile('&').split(a)
# #     for i in range(len(b)):
# #         if '($' in b[i]:
# #             re_com = re.compile('\$(.*?)\$')
# #             s = re_com.search(b[i]).group(1)
# #             c = re.sub(r'\$(.+?)\$', eval(s), a, 1)
# #             en_globe = re.compile('\((.*?)\)').findall(c)
# #             # for i in range (len(en_globe)):
# #             r = requests.get(url=config.PreHttp + 'getencrypt.json', params='plaintext='+en_globe[0])
# #             en_code = re.compile('"data":"(.*?)","message"').search(r.text).group(1)
# #             # g = re.compile(b[i].split('=')[0]+'=(.+?)').search(c).group(1)
# #             g = '('+en_globe[0]+')'
# #             a = c.replace(g, en_code)
# #         elif '(' in b[i] and '$' not in b[i]:
# #             en_globe1 = re.compile('\((.*?)\)').findall(b[i])
# #             # for i in range (len(en_globe)):
# #             r1 = requests.get(url=config.PreHttp + 'getencrypt.json', params='plaintext=' + en_globe1[0])
# #             en_code1 = re.compile('"data":"(.*?)","message"').search(r1.text).group(1)
# #             g1 = '('+en_globe1[0]+')'
# #             a = a.replace(g1, en_code1)
# #         elif  '$' in b[i] and '(' not in b[1]:
# #             re_com = re.compile('\$(.*?)\$')
# #             s1 = re_com.search(b[i]).group(1)
# #             c1 = re.sub(r'\$(.+?)\$', eval(s1), a, 1)
# #             a = c1
# # print(a)
#
# # c= 'aa(yyyy)bb'
# # f = c.replace(re.compile('a(.+?)b').search(c).group(1),'ttt')
# # print (f)
# # a = 'currentVersion=140'
# # b = dict([(e.split('=')[0], e.split('=')[1]) for e in a.split('&')])
# # print (b)
#
# import re
# a = '{"data":{"receivePrincipal":112.0000,"receiveInterest":0.00,"hasInterest":27.93,"annualRate":5.50,"addAnnualRate":1.00,"currentYesterdayIncome":0.01,"redeemTotalAmount":102.0100,"surplusAmount":149888.0000,"productSurplusAmount":1328290.0000},"message":"操作成功","code":"1","serviceDate":1493170138606}'
# # m=re.search('[0-9]+$', a)
# # print (a[m.start(1):m.end(2)])
# r = re.compile('"redeemTotalAmount":.*\.(.+?),"surplusAmount')
# b = r.search(a).group(1)
# print (b)

# import pymysql
# import re
#
#
#
# class DB:
#
#     conn = pymysql.connect(host='172.17.255.219', port=3306, user='root', passwd='123456', db='mtbill',use_unicode=True, charset="utf8")
#
#     def query(self, sql):
#         cur = self.conn.cursor()
#         cur.execute(sql)
#         for r in cur.fetchall():
#             return r
#             cur.close()
#         self.conn.close()
#
#     def get_code_sms(self):
#         code = self.query(
#             "SELECT smsParam FROM sms_record "
#             "WHERE smsParam like '%code%' "
#             " ORDER BY id DESC LIMIT 1;"
#             )
#         return str((re.compile(r'\d+').findall(str(code)))[0])
#
# print (DB().get_code_sms())
# import common
# import db
# common.sql_sms = db.DB().get_code_sms()
# print(common.sql_sms)
# import time
#
# time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#
# print(time_str)
# from pyh import *
# page = PyH('My wonderful PyH page')
# page << table(border="1px", cellspacing="0px",style="border-collapse:collapse;table-layout:fixed") << tr(td('1pioioioioioioioioiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',style="width:50px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis") + td('dddddddddddddddddddddddddddddddddddddddddd2',style="width:500px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis")) + tr(td('3') + td('4'))
# page << h2('Another way to build a 4 by 4 table')
# mytab = page << table()
# tr1 = mytab << tr()
# tr1 << td('1') + td('2')
# tr2 = mytab << tr()
# tr2 << td('3') + td('4')
# page.printOut()
# f = open('a.html', 'w')
# f.write(doctype)
# # f.write(str(page.render().encode('utf-8')))
# f.write(page.render())
# f.flush()
# f.close()
#
# from pyh import *
# page = PyH('My wonderful PyH page')
# # page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
# # page.addJS('myJavascript1.js', 'myJavascript2.js')
# page << h1('My big title', cl='center')
# page << div(cl='myCSSclass1 myCSSclass2', id='myDiv1') << p('I love PyH!', id='myP1')
# mydiv2 = page << div(id='myDiv2')
# mydiv2 << h2('A smaller title') + p('Followed by a paragraph.')
# page << div(id='myDiv3')
# page.myDiv3.attributes['cl'] = 'myCSSclass3'
# page.myDiv3 << p('Another paragraph')
# page.printOut()
# def test():
#     if 2>1:
#         return 1
#     print('aaa')

#coding=utf-8
import threading
from time import ctime,sleep

def music():
    for i in range(2):
        print ("I was listening to")
        return "aaa"

def move(func):
    for i in range(2):
        print ("I was at the")
        sleep(5)

threads = []
t1 = threading.Thread(target=music)
threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print ("all over %s")
    bb = music()
    print(bb)