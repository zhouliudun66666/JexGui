#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing


import Utils


class Service:

    # 登录
    def login(self,user,password):
        params = {
            'loginName': user,
            'password': password,
            'udesk': False,
            'sig': '',
            'token': '',
            'scene': '',
            'sso': '',
            'return_to': ''
            }
        url = '/api/v2/inner/user/weblogin'
        return Utils.Utils().http_post_request(params, url)

    # 二次验证登录
    def login_verify(self,dubbleGoogleCode,username,uuid):
        params = {
            'dubbleGoogleCode': dubbleGoogleCode,
            'username': username,
            'uuid': uuid
            }
        url = '/api/v2/inner/user/check'
        return Utils.Utils().http_post_request(params, url)

    # IP限制
    def ip_check(self):
        params = {
            }
        url = '/api/v2/inner/user/login/isIpAliCheck'
        return Utils.Utils().http_post_request(params, url)

    # 退出登录
    def login_out(self):
        params = {
            }
        url = '/api/v2/inner/user/logout'
        return Utils.Utils().http_post_request(params, url)

    # 交易
    def trade(self, price, amount, type, tradePassword, symbol, source):
        params = {
            'price': price,
            'amount': amount,
            'type': type,
            'tradePassword': tradePassword,
            'symbol': symbol,
            'source': source
            }
        url = '/api/v2/inner/trade/placeOrder'
        return Utils.Utils().http_post_request(params, url)

    # 撤单
    def cancel_buyorder(self,orderId, symbol, source):
        params = {
            'orderId': orderId,
            'symbol': symbol,
            'source': source
            }
        url = '/api/v2/inner/trade/cancelOrder'
        return Utils.Utils().http_post_request(params, url)

    # 首页index信息
    def get_index_info(self,lang):
        params = {
            'lang': lang
            }
        url = '/api/v2/pub/index/info'
        return Utils.Utils().http_get_request(params, url)

    # 首页指定市场K线数据
    def get_index_klines(self, market):
        params = {
            'market': market
            }
        url = '/api/v2/pub/index/klines'
        return Utils.Utils().http_get_request(params, url)

    # 获取K线信息
    def get_kline(self, symbol, type, size, frome, to):
        params = {
            'symbol': symbol,
            'type': type,
            'size': size,
            'from': frome,
            'to': to
        }
        url = '/api/v2/pub/kline'
        return Utils.Utils().http_get_request(params, url)

    # 获取ticker信息
    def get_ticker(self, symbol):
        params = {
            'symbol': symbol
            }
        url = '/api/v2/pub/ticker'
        return Utils.Utils().http_get_request(params, url)

    # 获取汇率信息
    def get_exchange(self):
        params = {
            }
        url = '/api/v2/pub/exchange'
        return Utils.Utils().http_get_request(params, url)

    # 获取所有交易对
    def get_symbol(self):
        params = {
            }
        url = '/api/v2/pub/symbols'
        return Utils.Utils().http_get_request(params, url)

    # 获取所有资产
    def get_currencys(self):
        params = {
            }
        url = '/api/v2/pub/currencys'
        return Utils.Utils().http_get_request(params, url)

    # 获取市场深度
    def get_depth(self, symbol, size):
        params = {
            'symbol': symbol,
            'size': size
            }
        url = '/api/v2/pub/depth'
        return Utils.Utils().http_get_request(params, url)

    # 获取交易信息
    def get_trades(self, symbol, since):
        params = {
            'symbol': symbol,
            'since': since
            }
        url = '/api/v2/pub/trades'
        return Utils.Utils().http_get_request(params, url)

    # 获取验证码
    def get_phone_code(self, csessionid, sig, token, scene, phone, type):
        params = {
            'csessionid': csessionid,
            'sig': sig,
            'token': token,
            'scene': scene,
            'phone': phone,
            'type': type
            }
        url = '/api/v2/verifiable/phonecode'
        return Utils.Utils().http_get_request(params, url)

    # 获取邮箱验证码
    def get_email_code(self, csessionid, sig, token, scene, email, type, lang):
        params = {
            'csessionid': csessionid,
            'sig': sig,
            'token': token,
            'scene': scene,
            'email': email,
            'type': type,
            'lang': lang
            }
        url = '/api/v2/inner/email/code'
        return Utils.Utils().http_get_request(params, url)

    # 注册
    def register(self, userName, code, password, passwordAgain, agreement):
        params = {
            'userName': userName,
            'code': code,
            'password': password,
            'passwordAgain': passwordAgain,
            'agreement': agreement,
            'channelId': '',
            'utmSource': ''
            }
        url = '/api/v2/inner/user/regist'
        return Utils.Utils().http_post_request(params, url)

    # 找回密码第一步
    def find_password_one(self, csessionid, sig, token, scene, userName, lang):
        params = {
            'csessionid': csessionid,
            'sig': sig,
            'token': token,
            'scene': scene,
            'userName': userName,
            'lang': lang
            }
        url = '/api/v2/inner/user/findPassword/checkUser'
        return Utils.Utils().http_post_request(params, url)


    # 找回密码第二步
    def find_password_two(self, userName, code):
        params = {
            'userName': userName,
            'code': code
            }
        url = '/api/v2/inner/user/findPassword/checkCode'
        return Utils.Utils().http_post_request(params, url)

    # 找回密码第三步
    def find_password_three(self, userName, newPassword, confirmPassword):
        params = {
            'userName': userName,
            'newPassword': newPassword,
            'confirmPassword': confirmPassword
            }
        url = '/api/v2/inner/user/findPassword/resetPassword'
        return Utils.Utils().http_post_request(params, url)

    # 委托记录缓存
    def get_entrust_record(self):
        params = {
        }
        url = '/api/v2/inner/trade/entrustRecord'
        return Utils.Utils().http_get_request(params, url)

    # 委托记录更多
    def get_order_record(self, symbolID, orderType, startDate, endDate, status, orderID, size):
        params = {
            'symbolID': symbolID,
            'orderType': orderType,
            'startDate': startDate,
            'endDate': endDate,
            'status': status,
            'orderID': orderID,
            'size': size
        }
        url = '/api/v2/inner/trade/orderRecord'
        return Utils.Utils().http_get_request(params, url)

    # 交易中心左侧ticker
    def get_market_ticker(self):
        params = {
        }
        url = '/api/v2/inner/market/coin/ticker'
        return Utils.Utils().http_get_request(params, url)

    # 交易中心右侧深度
    def get_market_depth(self, symbol):
        params = {
            'symbol': symbol
        }
        url = '/api/v2/inner/market/depth'
        return Utils.Utils().http_get_request(params, url)

    # 期权交易报价表
    def get_markert_option_ticker(self):
        params = {
        }
        url = '/api/v2/inner/market/option/ticker'
        return Utils.Utils().http_get_request(params, url)

    # 用户个人信息
    def user_account(self):
        params = {
        }
        url = '/api/v2/inner/user/account'
        return Utils.Utils().http_get_request(params, url)

    # 绑定邮箱
    def bind_email(self, email, dubbleGoogleCode, dubblePhoneCode, dubblePhoneMsgType):
        params = {
            'email': email,
            'dubbleGoogleCode': dubbleGoogleCode,
            'dubblePhoneCode': dubblePhoneCode,
            'dubblePhoneMsgType': dubblePhoneMsgType
            }
        url = '/api/v2/inner/user/bindEmail'
        return Utils.Utils().http_post_request(params, url)

    # 绑定谷歌验证器
    def bind_maf(self, code, dubblePhoneMsgType, dubblePhoneCode, dubbleGoogleCode):
        params = {
            'code': code,
            'dubblePhoneMsgType': dubblePhoneMsgType,
            'dubblePhoneCode': dubblePhoneCode,
            'dubbleGoogleCode': dubbleGoogleCode
            }
        url = '/api/v2/inner/user/bindMfa'
        return Utils.Utils().http_post_request(params, url)

    # Level1验证
    def certify_one(self, cardType, nation, bankId, userName, birthday, cardNum, bankCardNum, token):
        params = {
            'cardType': cardType,
            'nation': nation,
            'bankId': bankId,
            'userName': userName,
            'birthday': birthday,
            'cardNum': cardNum,
            'bankCardNum': bankCardNum,
            'token': token
            }
        url = '/api/v2/inner/user/certify'
        return Utils.Utils().http_post_request(params, url)

    # 获取谷歌验证码
    def get_maf(self):
        params = {
        }
        url = '/api/v2/inner/user/getMfa'
        return Utils.Utils().http_get_request(params, url)

    # 获取验证码（旧）
    def get_msg_code(self, phoneMsgType):
        params = {
            'phoneMsgType': phoneMsgType
        }
        url = '/user/getMsgCode.do'
        return Utils.Utils().http_post_request(params, url)

    # 我的邀请
    def invite(self):
        params = {
        }
        url = '/api/v2/inner/user/invite'
        return Utils.Utils().http_get_request(params, url)

    # 实名认证等级状态
    def get_level(self):
        params = {
        }
        url = '/api/v2/inner/user/level'
        return Utils.Utils().http_get_request(params, url)

    # 实名认证提交项目
    def level_items(self):
        params = {
        }
        url = '/api/v2/inner/user/levelItems'
        return Utils.Utils().http_get_request(params, url)

    # 重置登录密码
    def reset_pwd(self, newPwd, oldPwd, newPwdT):
        params = {
            'newPwd': newPwd,
            'oldPwd': oldPwd,
            'newPwdT': newPwdT
            }
        url = '/api/v2/inner/user/resetPwd'
        return Utils.Utils().http_post_request(params, url)

    # 安全策略信息
    def security_policy(self):
        params = {
        }
        url = '/api/v2/inner/user/securityPolicy'
        return Utils.Utils().http_get_request(params, url)

    # 发送绑定邮箱邮件
    def send_email(self):
        params = {
        }
        url = '/api/v2/inner/user/sendEmail'
        return Utils.Utils().http_get_request(params, url)

    # 修改登录二次交易策略
    def set_login_policy(self, code, type, dubbleGoogleCode, dubblePhoneMsgType, dubblePhoneCode):
        params = {
            'code': code,
            'type': type,
            'dubbleGoogleCode': dubbleGoogleCode,
            'dubblePhoneMsgType': dubblePhoneMsgType,
            'dubblePhoneCode': dubblePhoneCode,
            }
        url = '/api/v2/inner/user/setLoginPolicy'
        return Utils.Utils().http_post_request(params, url)

    # 绑定更换手机
    def set_mobile(self, phone, phoneMsgType, phoneCode, dubblePhoneCode, dubblePhoneMsgType, dubbleGoogleCode, status):
        params = {
            'phone': phone,
            'phoneMsgType': phoneMsgType,
            'phoneCode': phoneCode,
            'dubblePhoneCode': dubblePhoneCode,
            'dubblePhoneMsgType': dubblePhoneMsgType,
            'dubbleGoogleCode': dubbleGoogleCode,
            'status': status
            }
        url = '/api/v2/inner/user/setMobile'
        return Utils.Utils().http_post_request(params, url)

    # 设置资金密码
    def set_trade_pwd(self, pwd, pwdT, dubbleGoogleCode, dubblePhoneMsgType, dubblePhoneCode):
        params = {
            'pwd': pwd,
            'pwdT': pwdT,
            'dubbleGoogleCode': dubbleGoogleCode,
            'dubblePhoneMsgType': dubblePhoneMsgType,
            'dubblePhoneCode': dubblePhoneCode
            }
        url = '/api/v2/inner/user/setTradePwd'
        return Utils.Utils().http_post_request(params, url)

    # 解绑谷歌验证
    def unbind_mfa(self, dubblePhoneMsgType, dubblePhoneCode):
        params = {
            'dubblePhoneMsgType': dubblePhoneMsgType,
            'dubblePhoneCode': dubblePhoneCode
            }
        url = '/api/v2/inner/user/unBindMfa'
        return Utils.Utils().http_post_request(params, url)

    # 验证绑定邮箱邮件
    def verify_email(self, uuid, token):
        params = {
            'uuid': uuid,
            'token': token
        }
        url = '/api/v2/inner/user/verifyEmail'
        return Utils.Utils().http_get_request(params, url)

    # 取消提现
    def cancel_withdraw(self, assetType, id):
        params = {
            'assetType': assetType,
            'id': id
        }
        url = '/api/v2/inner/cancelWithdraw'
        return Utils.Utils().http_get_request(params, url)

    # 账户资产相关信息
    def get_finance(self, assetType):
        params = {
            'assetType': assetType
        }
        url = '/api/v2/inner/finance'
        return Utils.Utils().http_get_request(params, url)

    # 资金流水
    def get_account_recorde(self, assetType, handleType, startDate, endDate, pageNo, pageSize):
        params = {
            'assetType': assetType,
            'handleType': handleType,
            'startDate': startDate,
            'endDate': endDate,
            'pageNo': pageNo,
            'pageSize': pageSize,
        }
        url = '/api/v2/inner/finance/accountRecord'
        return Utils.Utils().http_get_request(params, url)

    # 添加地址
    def add_address(self, address, assetType, remark, isAuth, withdrawPassword, dubbleGoogleCode, dubblePhoneCode, dubblePhoneMsgType):
        params = {
            'address': address,
            'assetType': assetType,
            'remark': remark,
            'isAuth': isAuth,
            'withdrawPassword': withdrawPassword,
            'dubbleGoogleCode': dubbleGoogleCode,
            'dubblePhoneCode': dubblePhoneCode,
            'dubblePhoneMsgType': dubblePhoneMsgType
            }
        url = '/api/v2/inner/finance/addAddress'
        return Utils.Utils().http_post_request(params, url)

    # 地址管理
    def get_address(self, assetType):
        params = {
            'assetType': assetType
        }
        url = '/api/v2/inner/finance/address'
        return Utils.Utils().http_get_request(params, url)

    # 申请提现
    def apply_withdraw(self, assetType, addressId, withdrawFee, withdrawAmount, source, dubbleGoogleCode, dubblePhoneCode, dubblePhoneMsgType, withdrawPassword):
        params = {
            'assetType': assetType,
            'addressId': addressId,
            'withdrawFee': withdrawFee,
            'withdrawAmount': withdrawAmount,
            'source': source,
            'dubbleGoogleCode': dubbleGoogleCode,
            'dubblePhoneCode': dubblePhoneCode,
            'dubblePhoneMsgType': dubblePhoneMsgType,
            'withdrawPassword': withdrawPassword
            }
        url = '/api/v2/inner/finance/applyWithdraw'
        return Utils.Utils().http_post_request(params, url)

    # 提现邮件确认
    def withdraw_email_confirm(self, uuid, token):
        params = {
            'uuid': uuid,
            'token': token
        }
        url = '/api/v2/inner/finance/withdrawEmailConfirm'
        return Utils.Utils().http_get_request(params, url)

    # 删除地址
    def disable_coin_address(self, id):
        params = {
            'id': id
            }
        url = '/api/v2/inner/finance/disabledCoinAddress'
        return Utils.Utils().http_post_request(params, url)

    # 生成充值地址
    def get_coin_address(self, csessionid, sig, token, scene, assetType):
        params = {
            'csessionid': csessionid,
            'sig': sig,
            'token': token,
            'scene': scene,
            'assetType': assetType
            }
        url = '/api/v2/inner/finance/getCoinAddress'
        return Utils.Utils().http_get_request(params, url)

    # 充值信息
    def recharge_info(self, assetType):
        params = {
            'assetType': assetType
        }
        url = '/api/v2/inner/finance/recharge'
        return Utils.Utils().http_get_request(params, url)

    # 获取充值记录
    def get_recharge_recorde(self, assetType, start, end, frome, size):
        params = {
            'assetType': assetType,
            'start': start,
            'end': end,
            'frome': frome,
            'size': size
        }
        url = '/api/v2/inner/finance/rechargeRecord'
        return Utils.Utils().http_get_request(params, url)

    # 提现相关信息
    def get_withdraw_info(self, assetType):
        params = {
            'assetType': assetType
        }
        url = '/api/v2/inner/finance/withdraw'
        return Utils.Utils().http_get_request(params, url)

    # 提现记录
    def get_withdraw_recorde(self, assetType, start, end, frome, size):
        params = {
            'assetType': assetType,
            'start': start,
            'end': end,
            'frome': frome,
            'size': size
        }
        url = '/api/v2/inner/finance/withdrawRecord'
        return Utils.Utils().http_get_request(params, url)

    # 提现额度
    def get_finance_limit(self):
        params = {
        }
        url = '/api/v2/inner/finance/financeLimit'
        return Utils.Utils().http_get_request(params, url)

    # 相关操作的前置策略
    def get_pretoset(self):
        params = {
        }
        url = '/api/v2/pub/preToSetting'
        return Utils.Utils().http_get_request(params, url)

    # 站点通用信息
    def get_footer(self):
        params = {
        }
        url = '/api/v2/inner/footer'
        return Utils.Utils().http_get_request(params, url)

