#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import pymysql
import time
import MyException


class DB:

    # 数据库查询
    def get_dbdata(self, sql, db):
        conn = pymysql.connect(host='192.168.0.3', port=3306, user='digi', passwd='digi123456', db=db,
                               charset="utf8")
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
        cur.close()
        conn.close()

    # 查询订单
    def get_order(self, table, id):
        try:
            for i in range(3):
                order = DB().get_dbdata("SELECT turnover,deal_amount,status FROM {0} WHERE id ={1};".format(table, id), 'coin')
                if order !=():
                    order_list = list(map(str, order[0]))
                    return [float(i) for i in order_list]
                    break
                else:
                    time.sleep(5)
            if order ==():
                raise MyException.NotMatchException("没有订单记录")
                return False
        except Exception as ex:
            print(ex)

    # 查询最新价格
    def get_current_price(self,symbol):
        price = DB().get_dbdata("SELECT last FROM ticker WHERE symbol = {0};".format(symbol),'coin_sub')
        return float(str(price[0][0]))

    # 查询资金
    def get_balance(self,user_id,symbol_asset):
        user_balance = DB().get_dbdata("SELECT balance,lock_balance,settle_fee FROM user_balance "
                                       "WHERE user_id = {0} and asset_type = {1}".format(user_id, symbol_asset), 'coin')
        balance_list = list(map(str,user_balance[0]))
        return [float(i) for i in balance_list]

    # 查询资金流水记录
    def get_balance_flow(self , order_id , asset_type, user_id, table_pending=None):
        if table_pending != None:
            flow = DB().get_dbdata("SELECT amount, fee, after_amount FROM account_record ar LEFT JOIN {0} otp ON"
                                   " ar.object_id = otp.id WHERE otp.trade_orders_id = {1} and ar.asset_type = {2} and ar.user_id = {3} ".format(table_pending,order_id,asset_type,user_id), 'coin')
        else:
            flow = DB().get_dbdata("SELECT amount, fee, after_amount FROM account_record ar LEFT JOIN dock_trade_orders_finish dto ON"
                                   " ar.object_id = dto.id WHERE dto.id = {0} AND ar.asset_type = {1} and ar.user_id = {2}".format(order_id, asset_type,user_id),'coin')
        record_list = list(map(str, flow[0]))
        if record_list[1] == 'None':
            record_list[1] = 0
        return [float(i) for i in record_list]

    #查询交易费率
    def get_fee(self,symbol):
        fee = DB().get_dbdata("SELECT maker_fee FROM `symbol` WHERE id = {0} ;".format(symbol),'coin')
        return abs(float(str(fee[0][0])))

    #查询ticker
    def get_ticker(self,symbol, market_type):
        if market_type == 'coin':
            ticker_info = DB().get_dbdata(
                "SELECT symbol,high,low,last,`change`,volume FROM `ticker` WHERE symbol = {0};".format(symbol),'coin_sub')
        else:
            ticker_info = DB().get_dbdata(
                "SELECT symbol,high,low,last,`change` FROM `ticker` WHERE symbol = {0};".format(symbol),'coin_sub')
        ticker_info_list = list(map(str, ticker_info[0]))
        return [float(i) for i in ticker_info_list]
        # return ticker_info_list

    # 查询手机验证码
    def get_phoneCode(self, phone):
        code = DB().get_dbdata("SELECT code FROM `msg_code` WHERE phone = {0} ORDER BY id DESC LIMIT 1;".format(phone),
                               'coin_sub')
        return str(code[0][0])

    # 查询邮箱验证码
    def get_emailCode(self, email):
        code = DB().get_dbdata("SELECT params FROM `email_to_send` WHERE email='{0}' ORDER BY id DESC LIMIT 1;".format(email),
                               'coin_sub')
        return str(code[0][0])

    # 查询最近委托订单
    def get_latest_order(self,table1, table2, table3, user_id):
        order = DB().get_dbdata("SELECT type, trade_amount, trade_price, `status` ,created_date FROM {0} WHERE"
                                " user_id = {3} UNION ALL SELECT type, trade_amount, trade_price, `status` ,created_date FROM"
                                " {1} WHERE user_id = {3} UNION ALL "
                                "SELECT type, trade_amount, trade_price, `status` ,created_date FROM {2} WHERE"
                                " user_id = {3} ORDER BY created_date desc LIMIT 10;".format(table1,table2,table3,user_id),'coin')
        return order

    # 查询更多订单记录
    def get_more_order(self, table, user_id, symbol=None):
        if symbol is None:
            order = DB().get_dbdata("SELECT type, trade_amount, trade_price, `status` ,created_date FROM {0} WHERE"
                                " user_id = {1} ORDER BY created_date desc LIMIT 10;".format(table, user_id), 'coin')
        else:
            order = DB().get_dbdata("SELECT type, trade_amount, trade_price, `status` ,created_date FROM {0} WHERE"
                                " user_id = {1} AND symbol ={2} ORDER BY created_date desc LIMIT 10;".format(table, user_id, symbol), 'coin')
        return order

    # 查询地址
    def get_address(self, user_id, asset_type):
        address_info = DB().get_dbdata("SELECT id, address, `status` FROM `out_coin_address` WHERE user_id = {0} "
                                       " AND asset_type = {1} ORDER BY id DESC LIMIT 1;".format(user_id, asset_type), 'coin')
        return list(map(str, address_info[0]))

    # 提现记录
    def get_withdraw_record(self, table, user_id, asset_type, status):
        withdraw_record = DB().get_dbdata("SELECT id , `status` FROM `{0}` WHERE user_id = {1} and "
                                          "asset_type={2} AND `status` = {3};".format(table, user_id, asset_type, status), 'coin')
        return list(map(str, withdraw_record[0]))

# print(DB().get_current_order('trade_orders_14', 'dock_trade_orders', 'trade_orders_77', 350956))

