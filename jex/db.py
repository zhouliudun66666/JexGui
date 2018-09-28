#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

import pymysql
import re
import time
import common

class DB:

    def query(self, sql):
        conn = pymysql.connect(host='172.17.255.219', port=3306, user='root', passwd='123456', db='mtbill',
                               use_unicode=True, charset="utf8")
        cur = conn.cursor()
        cur.execute(sql)
        for r in cur.fetchall():
            return r
            cur.close()
        conn.close()

    def get_code_sms(self):
        code = self.query(
            "SELECT smsParam FROM sms_record WHERE smsParam like '%code%' ORDER BY id DESC LIMIT 1;"
            )
        return str((re.compile(r'\d+').findall(str(code)))[0])

    def get_product_id(self, productType, productArea):
        product_id = self.query(
            "SELECT id FROM `product` "
            "WHERE `status` = 2 AND productType = " + str(productType) + " AND productArea = " + str(productArea) + " AND surplusAmount >= 100 LIMIT 1;"
        )
        return str((re.compile(r'\d+').findall(str(product_id)))[0])

    def make_product(self):
        id = self.query("SELECT id FROM `product` ORDER BY id DESC LIMIT 1;")
        idint = int((re.compile(r'\d+').findall(str(id)))[0]) + 1
        time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        conn = pymysql.connect(host='172.17.255.219', port=3306, user='root', passwd='123456', db='mtbill',
                               use_unicode=True, charset="utf8")
        cur = conn.cursor()
        cur.execute("INSERT INTO `product` VALUES (" + str(idint) + ", '银票直投"+ time_str +"', '300.0000', '6.50', null, '300.0000', '0.0000',"
                     " '0.00', '12', '2', '1', '1', '1', null, null, '2017-04-27 02:30:01', '2017-04-27 02:30:01', null, null,"
                     " '2017-04-27 02:30:01', '3', '100.00', '20000.00', '100.00', '0000-00-00 00:00:00', '0.00', null, null, 1 ,null,0,0);")
        conn.commit()
        conn.close()
        common.productID = str(idint)

# print(DB().get_code_sms())
# investID = self.query("SELECT id FROM `invest` WHERE 'productId'=" + str(idint) + " ORDE R BY id DESC LIMIT 1;")
# DB().make_product()