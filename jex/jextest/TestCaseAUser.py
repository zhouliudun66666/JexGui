#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import Service, Common, DB, ComMeth, Utils


class TestCaseUser(unittest.TestCase):

    SUCCESS_RESULT = "'code': 0"

    def setUp(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)

    def tearDown(self):
        time.sleep(1)

    # # 通过手机号注册
    # def test101_register_by_phone(self):
    #     '''通过手机号注册'''
    #     print('register_by_phone')
    #     try:
    #         response = Service.Service().register(Common.teleNum, ComMeth.ComMeth().get_code(Common.teleNum, 18),
    #                                               Common.pwdOne, Common.pwdOne, 'true')
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         token = response['data']['token']
    #         Utils.Utils.headers['headerToken'] = token
    #         print(Common.teleNum)
    #         print(token)
    #     except Exception as ex:
    #         raise ex
    #
    # # 通过邮箱注册
    # def test102_register_by_email(self):
    #     '''通过邮箱注册'''
    #     print('register_by_email')
    #     try:
    #         response = Service.Service().register(Common.email, ComMeth.ComMeth().get_code_regist_email(Common.email, 20, 0),
    #                                               Common.pwdOne, Common.pwdOne, 'true')
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(Common.email)
    #     except Exception as ex:
    #         raise ex
    #
    # # 绑定邮箱
    # def test102_bind_email(self):
    #     '''绑定邮箱'''
    #     print('bind_email')
    #     try:
    #         response = Service.Service().bind_email(Common.email, None, ComMeth.ComMeth().get_code(Common.teleNum, 21), 21)
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 获取谷歌验证码
    # def test503_get_mfa(self):
    #     '''获取谷歌验证码'''
    #     print('get_mf')
    #     try:
    #         response = Service.Service().get_maf()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 我的邀请
    # def test504_invite(self):
    #     '''我的邀请'''
    #     print('invite')
    #     try:
    #         response = Service.Service().invite()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 实名认证信息
    # def test505_user_level(self):
    #     '''实名认证信息'''
    #     print('user_level')
    #     try:
    #         response = Service.Service().get_level()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 实名认证提交项目
    # def test506_level_items(self):
    #     '''实名认证提交项目'''
    #     print('level_items')
    #     try:
    #         response = Service.Service().level_items()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 重置登录密码
    # def test507_reset_pwd(self):
    #     '''重置登录密码'''
    #     print('reset_pwd')
    #     try:
    #         response = Service.Service().level_items()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 安全策略设置页面信息
    # def test508_security_policy(self):
    #     '''安全策略设置页面信息'''
    #     print('security_policy')
    #     try:
    #         response = Service.Service().security_policy()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 发送绑定邮箱邮件
    # def test509_send_email(self):
    #     '''发送绑定邮箱邮件'''
    #     print('send_email')
    #     try:
    #         response = Service.Service().send_email()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # LEVEL2认证
    #
    # # 修改登录二次交易策略
    # def test510_set_login_policy(self):
    #     '''修改登录二次交易策略'''
    #     print('set_login_policy')
    #     try:
    #         response = Service.Service().set_login_policy()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 绑定或更换手机号
    # def test511_set_mobile(self):
    #     '''绑定或更换手机号'''
    #     print('set_mobile')
    #     try:
    #         response = Service.Service().set_mobile(Common.teleNum, 17, ComMeth.ComMeth().get_code(Common.teleNum), )
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 设置资金密码
    # def test512_set_trade_pwd(self):
    #     '''设置资金密码'''
    #     print('set_trade_pwd')
    #     try:
    #         response = Service.Service().set_trade_pwd(Common.pwdTwo, Common.pwdTwo, )
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 解绑谷歌验证码
    # def test513_unbind_mfa(self):
    #     '''解绑谷歌验证码'''
    #     print('unbind_mfa')
    #     try:
    #         response = Service.Service().unbind_mfa(9, ComMeth.ComMeth().get_code(Common.teleNum, 9))
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 验证绑定邮箱邮件
    # def test514_verify_email(self):
    #     '''验证绑定邮箱邮件'''
    #     print('verify_email')
    #     try:
    #         response = Service.Service().verify_email()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex

    # # 用户个人信息
    # def test501_user_info(self):
    #     '''用户个人信息'''
    #     print('user_info')
    #     try:
    #         response = Service.Service().user_account()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #         print(response)
    #     except Exception as ex:
    #         raise ex
    #
    # # 测试通过手机找回登录密码
    # def test103_find_password_by_phone(self):
    #     '''通过手机找回登录密码'''
    #     print('test_find_password_by_phone')
    #     try:
    #         response_one = Service.Service().find_password_one(Common.Aliyun_list[0].strip('\n'),
    #                                                            Common.Aliyun_list[1].strip('\n'),
    #                                                            Common.Aliyun_list[2].strip('\n'), 'register',
    #                                                            Common.teleNum, 0)
    #         Common.search_str(str(response_one), [self.SUCCESS_RESULT])
    #         for i in range(3):
    #             del Common.Aliyun_list[0]
    #         response_two = Service.Service().find_password_two(Common.teleNum, DB.DB().get_phoneCode(Common.teleNum))
    #         Common.search_str(str(response_two), [self.SUCCESS_RESULT])
    #         response_three = Service.Service().find_password_three(Common.teleNum,
    #                                                                Common.pwdOne, Common.pwdOne)
    #         Common.search_str(str(response_three), [self.SUCCESS_RESULT])
    #     except Exception as ex:
    #         raise ex
    #
    # # 测试通过邮箱找回登录密码
    # def test104_find_password_by_email(self):
    #     '''通过邮箱找回登录密码'''
    #     print('test_find_password_by_email')
    #     try:
    #         response_one = Service.Service().find_password_one(Common.Aliyun_list[0].strip('\n'),
    #                                                            Common.Aliyun_list[1].strip('\n'),
    #                                                            Common.Aliyun_list[2].strip('\n'), 'register',
    #                                                            Common.email, 0)
    #         Common.search_str(str(response_one), [self.SUCCESS_RESULT])
    #         for i in range(3):
    #             del Common.Aliyun_list[0]
    #         response_two = Service.Service().find_password_two(Common.email,
    #                                                            DB.DB().get_emailCode(Common.email))
    #         Common.search_str(str(response_two), [self.SUCCESS_RESULT])
    #         response_three = Service.Service().find_password_three(Common.email,
    #                                                                Common.pwdOne, Common.pwdOne)
    #         Common.search_str(str(response_three), [self.SUCCESS_RESULT])
    #     except Exception as ex:
    #         raise ex
    #
    # # 测试退出登录
    # def test207_loginout(self):
    #     '''退出登录'''
    #     print('test_loginout')
    #     try:
    #         response = Service.Service().login_out()
    #         Common.search_str(str(response), [self.SUCCESS_RESULT])
    #     except Exception as ex:
    #         raise ex
    #
    # # 使用邮箱登录(需要二次验证)
    # def test105_login_by_email(self):
    #     '''使用邮箱登录(需要二次验证)'''
    #     print('test_login_by_email')
    #     try:
    #         response_one = Service.Service().login('753057614@qq.com', Common.pwdOne)
    #         Utils.Utils.headers['headerToken'] = response_one['data']['token']
    #         Common.search_str(str(response_one), [self.SUCCESS_RESULT])
    #         response_two = Service.Service().login_verify(Common.generate_otp('HZTERXEO7C2655JP'), '753057614@qq.com',
    #                                                       response_one['data']['uuid'])
    #         Common.search_str(str(response_two), [self.SUCCESS_RESULT])
    #         # token = response_two['data']['token']
    #         # Utils.Utils.headers['headerToken'] = token
    #     except Exception as ex:
    #         raise ex

    # 使用手机登录(需要二次验证)
    def test109_login_by_phone(self):
        '''使用手机登录'''
        try:
            print('test_login_by_phone')
            response = ComMeth.ComMeth().login('18349192602')
            Common.search_str(str(response), [self.SUCCESS_RESULT])
        except Exception as ex:
            raise ex
