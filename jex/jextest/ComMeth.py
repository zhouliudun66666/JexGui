#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import Service, Common, DB, Utils


class ComMeth(unittest.TestCase):

    SUCCESS_RESULT = "'code': 0"

    def trade(self, symbol, rate, type, amount, tradePassword, source, user_id, symbol_asset, base_asset, table, tabel_pending=None, flag=None):
        try:
            old_balance_symbol = DB.DB().get_balance(user_id,symbol_asset)[0]
            old_balance_base = DB.DB().get_balance(user_id,base_asset)[0]
            trade_price = round(DB.DB().get_current_price(symbol) * rate, 8)
            response = Service.Service().trade(trade_price, amount, type, tradePassword, symbol, source)
            print(response)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            order_id = response['data']['id']
            order = DB.DB().get_order(table,order_id)
            self.assertEqual(order[2], 2, msg="订单信息错误")
            new_balance_symbol = DB.DB().get_balance(user_id,symbol_asset)[0]
            new_balance_base = DB.DB().get_balance(user_id,base_asset)[0]
            amount_record_base = DB.DB().get_balance_flow(order_id,base_asset,user_id, tabel_pending)
            amount_record_symbol = DB.DB().get_balance_flow(order_id,symbol_asset,user_id, tabel_pending)
            if type == 1:
                if flag != 'option':
                    self.assertEqual(abs(amount_record_symbol[1]), round(DB.DB().get_fee(symbol) * amount, 8), msg="手续费错误")
                self.assertEqual(new_balance_symbol, old_balance_symbol + order[1] - abs(amount_record_symbol[1]),
                                 msg="账户资产错误。")
                self.assertEqual(new_balance_base, round(old_balance_base - order[0], 11), msg="账户资产错误。。")
            elif type == 2:
                self.assertEqual(abs(amount_record_base[1]), round(DB.DB().get_fee(symbol) * order[0], 8), msg="手续费错误")
                self.assertEqual(new_balance_symbol, old_balance_symbol - order[1], msg="账户资产错误。")
                self.assertEqual(new_balance_base, old_balance_base + order[0] - abs(amount_record_base[1]), msg="账户资产错误。。")
            self.assertEqual(round(amount_record_symbol[0] - amount_record_symbol[2], 8), abs(amount_record_symbol[1]),msg="资金流水错误。")
            self.assertEqual(round(amount_record_base[0] - amount_record_base[2], 8), abs(amount_record_base[1]), msg="资金流水错误。。")
        except Exception as ex:
            raise ex

    def cancel_trade(self,symbol,rate,type,amount,tradePassword, source, user_id, asset, table):
        try:
            old_asset = DB.DB().get_balance(user_id,asset)
            trade_price = round(DB.DB().get_current_price(symbol) * rate, 8)
            response_trade = Service.Service().trade(trade_price, amount, type, tradePassword, symbol, source)
            allm = response_trade['data']['allMoney']
            order_id = response_trade['data']['id']
            new_lock_asset = DB.DB().get_balance(user_id, asset)[1]
            if type ==1:
                self.assertEqual(float(allm), round(new_lock_asset - old_asset[1], 8), msg="冻结金额错误。")
            else:
                self.assertEqual(amount, round(new_lock_asset - old_asset[1], 8), msg="冻结金额错误。。")
            time.sleep(1)
            response = Service.Service().cancel_buyorder(order_id, symbol, source)
            print(response)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            order = DB.DB().get_order(table, order_id)
            self.assertEqual(order[2], -1, msg="订单信息错误")
            self.assertEqual(DB.DB().get_balance(user_id,asset)[1], old_asset[1], msg="冻结金额未解冻")
            self.assertEqual(DB.DB().get_balance(user_id,asset)[0], old_asset[0], msg="账户资金错误")
        except Exception as ex:
            raise ex

    def check_ticker(self,list_coin,market_type):
        try:
            for i in range(len(list_coin)):
                btc_coin = list_coin[i]
                if market_type == 'coin':
                    btc_coin_info = [btc_coin['symbol'], btc_coin['high'], btc_coin['low'], btc_coin['last'],
                                     btc_coin['rate'].rstrip('%').replace(',',''), btc_coin['volume']]
                elif market_type == 'index':
                    btc_coin_info = [btc_coin['symbol'], btc_coin['high'], btc_coin['low'], btc_coin['index'],
                                     btc_coin['rate'].rstrip('%').replace(',','')]
                elif market_type =='option':
                    btc_coin_info = [btc_coin['symbol'], btc_coin['high'], btc_coin['low'], btc_coin['last'],
                                     btc_coin['rate'].rstrip('%').replace(',','')]
                btc_coin_info_float = [float(i) for i in btc_coin_info]
                # print(btc_coin_info_float)
                db_coin_info = DB.DB().get_ticker(btc_coin_info[0], market_type)
                # print(db_coin_info)
                self.assertEqual(btc_coin_info_float, db_coin_info, msg="首页市场信息数据不正确")
        except Exception as ex:
            raise ex

    # 获取手机验证码
    def get_code(self, phone, type):
        try:
            Service.Service().get_phone_code(Common.Aliyun_list[0].strip('\n'), Common.Aliyun_list[1].strip('\n'),
                                             Common.Aliyun_list[2].strip('\n'), 'register', phone, type)
            for i in range(3):
                del Common.Aliyun_list[0]
            return DB.DB().get_phoneCode(phone)
        except Exception as ex:
            raise ex

    def get_code_noali(self, type, phone):
        try:
            Service.Service().get_phone_code(None, None, None, None, None, type)
            return DB.DB().get_phoneCode(phone)
        except Exception as ex:
            raise ex

    # 注册获取邮箱验证码
    def get_code_regist_email(self, email,  type, lang):
        try:
            Service.Service().get_email_code(Common.Aliyun_list[0].strip('\n'), Common.Aliyun_list[1].strip('\n'),
                                             Common.Aliyun_list[2].strip('\n'), 'register', email, type, lang)
            for i in range(3):
                del Common.Aliyun_list[0]
            return DB.DB().get_emailCode(email)
        except Exception as ex:
            raise ex


    # 登录
    def login(self, username):
        try:
            response = Service.Service().login(username, Common.pwdOne)
            token = response['data']['token']
            Utils.Utils.headers['headerToken'] = token
            print(token)
            return response
        except Exception as ex:
            raise ex

