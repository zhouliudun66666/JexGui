# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# #  @author: WuBingBing
#
# import unittest
# import time
# from jextest import Service, Common, ComMeth
#
#
# class TestCaseOther(unittest.TestCase):
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
#     # 首页index
#     def test401_index(self):
#         print('index')
#         try:
#             response = Service.Service().get_index_info(0)
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#             coin = response['data']
#             a = coin['coinMarkets']
#             for i in [a['btc'], a['eth'], a['usdt']]:
#                 ComMeth.ComMeth().check_ticker(i, 'coin')
#             b = coin['indexMarket']
#             ComMeth.ComMeth().check_ticker(b, 'index')
#             c = coin['optionMarket']
#             ComMeth.ComMeth().check_ticker(c, 'option')
#         except Exception as ex:
#             raise ex
#
#     # 首页市场Klines
#     def test402_index_klines(self):
#         try:
#             print('index_klines')
#             for i in (-1, 1, 2 ,10, 13):
#                 response = Service.Service().get_index_klines(i)
#                 Common.search_str(str(response), [self.SUCCESS_RESULT])
#                 print(response)
#         except Exception as ex:
#             raise ex
#
#     # 汇率信息
#     def test403_exchange(self):
#         print('exchange')
#         try:
#             response = Service.Service().get_exchange()
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#             print(response)
#         except Exception as ex:
#             raise ex
#
#     # 所有交易对信息
#     def test404_all_symbol(self):
#         print('all_symbol')
#         try:
#             response = Service.Service().get_symbol()
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#             print(response)
#         except Exception as ex:
#             raise ex
#
#     # 获取所有资产
#     def test405_all_assert(self):
#         print('all_assert')
#         try:
#             response = Service.Service().get_currencys()
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#             print(response)
#         except Exception as ex:
#             raise ex
#
#     # 获取市场深度
#     def test406_depth(self):
#         print('depth')
#         try:
#             for symbol in ['eth/btc', 'eos/usdt', '周EOS看涨0423']:
#                 response = Service.Service().get_depth(symbol, 30)
#                 Common.search_str(str(response), [self.SUCCESS_RESULT])
#                 print(response)
#         except Exception as ex:
#             raise ex
#
#     # 获取K线信息
#     def test407_kline(self):
#         print('kline')
#         try:
#             for symbol in ['eth/btc', 'eos/usdt', '周EOS看涨0423']:
#                 for time_type in ['5min', '60min', '1day', '1week']:
#                     response = Service.Service().get_kline(symbol, time_type, 100, None, None)
#                     Common.search_str(str(response), [self.SUCCESS_RESULT])
#                     print(response)
#         except Exception as ex:
#             raise ex
#
#     # 获取ticker信息
#     def test408_ticker(self):
#         print('ticker')
#         try:
#             for symbol in ['eth/btc', 'eos/usdt', '周EOS看涨0423']:
#                 response = Service.Service().get_ticker(symbol)
#                 Common.search_str(str(response), [self.SUCCESS_RESULT])
#                 print(response)
#         except Exception as ex:
#             raise ex
#
#     # 获取交易信息
#     def test409_trades(self):
#         print('trades')
#         try:
#             for symbol in ['eth/btc', 'eos/usdt', '周EOS看涨0423']:
#                 response = Service.Service().get_trades(symbol, None)
#                 Common.search_str(str(response), [self.SUCCESS_RESULT])
#                 print(response)
#         except Exception as ex:
#             raise ex
#
#     # 相关操作的前置策略
#     def test410_get_pretoset(self):
#         try:
#             response = Service.Service().get_pretoset()
#             Common.search_str(str(response), [self.SUCCESS_RESULT])
#             print(response)
#         except Exception as ex:
#             raise ex
#
#
#
#
