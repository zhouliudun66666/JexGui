# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# #  @author: WuBingBing
#
# import unittest
# import time
# from jextest import Service, Common, ComMeth
#
#
# class TestCaseEdit(unittest.TestCase):
#
#     SUCCESS_RESULT = "'code': 0"
#
#     def setUp(self):
#         time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#         print(time_str)
#
#     def tearDown(self):
#         time.sleep(1)
#
#     # 买入下单 JEX/BTC
#     def test301_trade_buy_mine(self):
#         '''本平台交易对买入下单'''
#         print('test_trade_buy_mine')
#         ComMeth.ComMeth().trade(14, 1.1, 1, 1, Common.pwdTwo, 0, 350956, 12, 1, 'trade_orders_finish_14', 'trade_orders_pending_14')
#
#     # 卖出下单 JEX/BTC
#     def test302_trade_sell_mine(self):
#         '''本平台交易对卖出下单'''
#         print('test_trade_sell_mine')
#         ComMeth.ComMeth().trade(14, 0.9, 2, 1, Common.pwdTwo, 0, 350956, 12, 1, 'trade_orders_finish_14', 'trade_orders_pending_14')
#
#     # 撤销买入订单JEX/BTC
#     def test303_cancel_buy_mine(self):
#         '''本平台交易对撤销买入下单'''
#         print('test_cancel_buy_mine')
#         ComMeth.ComMeth().cancel_trade(14, 0.5, 1, 1, Common.pwdTwo, 0, 350956, 1, 'trade_orders_finish_14')
#
#     # 撤销卖出订单JEX/BTC
#     def test304_cancel_sell_mine(self):
#         '''本平台交易对撤销卖出下单'''
#         print('test_cancel_sell_mine')
#         ComMeth.ComMeth().cancel_trade(14, 1.5, 2, 1, Common.pwdTwo, 0, 350956, 12, 'trade_orders_finish_14')
#
#     # 买入期权下单 周ETH-USDT看涨01
#     def test305_trade_buy_option(self):
#         '''期权买入下单'''
#         print('test_trade_buy_option')
#         ComMeth.ComMeth().trade(118, 1.1, 1, 1, Common.pwdTwo, 0, 350956, 83, 10, 'trade_orders_finish_118', 'trade_orders_pending_118', flag='option')
#
#     # 卖出期权下单 周ETH-USDT看涨01
#     def test306_trade_sell_option(self):
#         '''期权卖出下单'''
#         print('test0_trade_sell_option')
#         ComMeth.ComMeth().trade(118, 0.9, 2, 1, Common.pwdTwo, 0, 350956, 83, 10, 'trade_orders_finish_118', 'trade_orders_pending_118', flag='option')
#
#     # 撤销期权买入订单 周ETH-USDT看涨01
#     def test307_cancel_option_buy(self):
#         '''撤销期权买入下单'''
#         print('test_cancel_option_buy')
#         ComMeth.ComMeth().cancel_trade(118, 0.5, 1, 1, Common.pwdTwo, 0, 350956, 10, 'trade_orders_finish_118')
#
#     # 撤销期权卖出订单 周ETH-USDT看涨01
#     def test308_cancel_option_sell(self):
#         '''撤销期权卖出下单'''
#         print('test_cancel_option_sell')
#         ComMeth.ComMeth().cancel_trade(118, 1.5, 2, 1, Common.pwdTwo, 0, 350956, 83, 'trade_orders_finish_118')
#
#     # 火币买入下单 GNT/ETH
#     def test309_huobi_buy(self):
#         '''火币交易对买入下单'''
#         print('test_huobi_buy')
#         ComMeth.ComMeth().trade(102, 1.05, 1, 1, Common.pwdTwo, 0, 350956, 58, 2, 'dock_trade_orders_finish')
#
#     # 火币卖出下单 GNT/ETH
#     def test310_huobi_sell(self):
#         '''火币交易对卖出下单'''
#         print('test_huobi_sell')
#         ComMeth.ComMeth().trade(102, 0.95, 2, 1, Common.pwdTwo, 0, 350956, 58, 2, 'dock_trade_orders_finish')
#
#     # 火币撤销买入 GNT/ETH
#     def test311_cancel_huobi_buy(self):
#         '''火币交易对撤销买入下单'''
#         print('test_cancel_huobi_buy')
#         ComMeth.ComMeth().cancel_trade(102, 0.5, 1, 1, Common.pwdTwo, 0, 350956, 2, 'dock_trade_orders_finish')
#
#     # 火币撤销卖出 GNT/ETH
#     def test312_cancel_huobi_sell(self):
#         '''火币交易对撤销卖出下单'''
#         print('test_cancel_huobi_sell')
#         ComMeth.ComMeth().cancel_trade(102, 1.5, 2, 1, Common.pwdTwo, 0, 350956, 58, 'dock_trade_orders_finish')
#
#     # 委托记录缓存
#     def test313_enthrust_record(self):
#         '''查询缓存委托记录'''
#         print('enthrust_record')
#         try:
#             response = Service.Service().get_entrust_record()
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#             print(response)
#         except Exception as ex:
#             raise ex
#
#     # 委托记录更多
#     def test314_order_more_recorde(self):
#         '''查询更多委托记录'''
#         print('order_more_recorde')
#         try:
#             response = Service.Service().get_order_record(102, 1, '2018-05-01 00:00:00', '2018-05-02 00:00:00',
#                                                           '2,-1,8,', 1, 100)
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#             print(response)
#         except Exception as ex:
#             raise ex
#
#     # 交易中心ticker
#     def test314_market_ticker(self):
#         '''获取交易中心ticker数据'''
#         print('market_ticker')
#         try:
#             response = Service.Service().get_market_ticker()
#             print(response)
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#         except Exception as ex:
#             raise ex
#
#     # 交易中心深度信息
#     def test315_market_depth(self):
#         '''获取交易中心深度信息'''
#         print('market_depth')
#         try:
#             response = Service.Service().get_market_depth(14)
#             print(response)
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#         except Exception as ex:
#             raise ex
#
#     # 期权交易报价表
#     def test316_market_option_ticker(self):
#         '''期权交易报价表'''
#         print('market_option_ticker')
#         try:
#             response = Service.Service().get_markert_option_ticker()
#             print(response)
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#         except Exception as ex:
#             raise ex
#
#
#
