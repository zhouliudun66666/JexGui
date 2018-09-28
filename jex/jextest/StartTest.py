#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import unittest
import time
import HTMLTestRunner

if __name__ == '__main__':
    # suite = unittest.defaultTestLoader.discover('.', pattern='TestCase*.py')
    # time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # filename = "C:\\Data\\jex\\TestReport_" + time_str + ".html"
    # print (filename)
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #             stream=fp,
    #             title=u'JEX接口自动化测试报告',
    #             # description=u'【测试报告详情】：'
    #             )
    # runner.run(suite)
    # fp.close()

    suite = unittest.defaultTestLoader.discover('.', pattern='TestCase*.py')
    unittest.TextTestRunner().run(suite)
