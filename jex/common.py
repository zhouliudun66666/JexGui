#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

import re
import time, random

List0 = []
globe_para = []
globe_para1 = []
globe_para0 = []
token = []
response = None
header_cookie = None
sql_sms = None
sql_productId_plan = None
sql_productId_sporadic = None
sql_productId_new = None
en_globe = []
acc_sid = None
SESSIONID = None
productID = None
progress = None


teleNum = random.choice(['150', '137', '189', '170']) + ''.join(random.choice('0123456789') for i in range(8))


class Common:

    def get_matchstr(self, str0, str1, n):
        try:
            re_com = re.compile(str1)
            matchstr = re_com.search(str0).group(n)
            return matchstr
        except AttributeError:
            print("断言错误!")


    def make_id(self):
        ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
        t = time.localtime()[0]
        x = '421381' + '%04d%02d%02d%03d' % (
            random.randint(t - 80, t - 18),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(1, 999))
        y = 0
        for i in range(17):
            y += int(x[i]) * ARR[i]

        return '%s%s' % (x, LAST[y % 11])


    def make_card(self, bankName):

        bank = {'招商银行': ('621485', 16),
                '光大银行': ('622666', 16),
                '中信银行': ('621773', 16),
                '建设银行': ('622700', 19),
                '农业银行': ('622848', 19),
                '工商银行': ('622202', 19),
                '兴业银行': ('622908', 16),
                '邮储银行': ('621098', 19),
                '广发银行': ('622556', 16),
                '交通银行': ('622259', 17),
                '民生银行': ('622620', 16),
                '中国银行': ('621790', 19),
                '平安银行': ('621626', 19)
                }
        cardNO1 = ''.join(random.choice('0123456789') for i in range(bank[bankName][1] - 7))
        cardNO2 = bank[bankName][0] + cardNO1
        c = tuple(cardNO2)
        s1 = 0
        s2 = 0
        for i in range(bank[bankName][1] - 1):
            if i % 2 == 0:
                a = int(c[(bank[bankName][1] - 2) - i]) * 2
                b = tuple(str(a))
                if len(b) == 2:
                    s1 = s1 + int(b[0]) + int(b[1])
                else:
                    s1 = s1 + a
            else:
                d = int(c[(bank[bankName][1] - 2) - i])
                s2 = s2 + d

        e = tuple(str(s1 + s2))
        f = int(e[len(e) - 1])
        if f == 0:
            n = 0
        else:
            n = 10 - f
        cardNO = cardNO2 + str(n)
        return cardNO






