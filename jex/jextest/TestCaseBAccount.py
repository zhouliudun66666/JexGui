#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import Service, Common, ComMeth, DB


class TestCaseAccount(unittest.TestCase):

    SUCCESS_RESULT = "'code': 0"

    def setUp(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)

    def tearDown(self):
        time.sleep(1)

    # 账户资产
    def test201_finance(self):
        '''账户资产'''
        print('finance')
        try:
            response = Service.Service().get_finance(1)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # 资金流水
    def test202_account_record(self):
        '''资金流水'''
        print('account_record')
        try:
            response = Service.Service().get_account_recorde(-1, -1, '2018-5-01', '2018-5-31', 1, 10)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # 添加地址
    def test203_add_address(self):
        '''添加地址'''
        print('add_address')
        try:
            response = Service.Service().add_address('19kAqGjL8qQeoXJw6xQ6KSCMKoVDnJeeeo', 1, 'coinfex', 'false',
                                                     Common.pwdTwo, Common.generate_otp('ZMUMVRAY6XEBGSOB'),
                                                     ComMeth.ComMeth().get_code(18938012345, 24), 24)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # 地址管理
    def test204_address(self):
        '''地址管理'''
        print('address')
        try:
            response = Service.Service().get_address(1)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # 删除地址
    def test205_disable_address(self):
        '''删除地址'''
        print('disable_address')
        try:
            response = Service.Service().disable_coin_address(DB.DB().get_address(350956, 1)[0])
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # 生成火币充值地址
    def test206_makeCoinAddress(self):
        '''生成火币地址'''
        try:
            print('makeCoinAddress')
            response = Service.Service().get_coin_address(Common.Aliyun_list[0].strip('\n'),
                                                          Common.Aliyun_list[1].strip('\n'),
                                                          Common.Aliyun_list[2].strip('\n'),
                                                          'register', 73)
            print(response)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex

    # 获取充值记录
    def test207_get_recharge_record(self):
        '''获取充值记录'''
        print('get_recharge_record')
        try:
            response = Service.Service().get_recharge_recorde(58, '2018-01-01 00:00:00', '2018-05-01 00:00:00', 1, 100)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # 提现记录
    def test208_get_withdraw_record(self):
        '''提现记录'''
        print('get_withdraw_record')
        try:
            response = Service.Service().get_withdraw_recorde(58, '2018-01-01 00:00:00', '2018-05-01 00:00:00', 1, 100)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # 申请提现
    def test209_apply_withdraw(self):
        '''申请提现'''
        print('apply_withdraw')
        try:
            response = Service.Service().apply_withdraw(1, 6264, 0.001, 0.01, 0, Common.generate_otp('HZTERXEO7C2655JP'),
                                                        ComMeth.ComMeth().get_code_noali(1, 18938012345), 1, Common.pwdTwo)
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # 取消提现
    def test210_cancel_withdraw(self):
        '''取消提现'''
        print('cancle_withdraw')
        try:
            response = Service.Service().cancel_withdraw(1, DB.DB().get_withdraw_record('out_coin_transaction', 350956, 1, 1)[0])
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

    # # 提现邮件确认
    # def test211_withdraw_confirm(self):
    #     '''提现邮件确认'''
    #     print('withdraw_confirm')
    #     try:
    #         response = Service.Service().withdraw_email_confirm()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex

    # 提现额度
    def test212_finance_limit(self):
        '''获取提现额度'''
        print('finance_limit')
        try:
            response = Service.Service().get_finance_limit()
            Common.search_str(str(response), [self.SUCCESS_RESULT])
            print(response)
        except Exception as ex:
            raise ex

