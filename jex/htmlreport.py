#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

from pyh import *

TestCaseNo = []
Response = []
Result = []
Request = []
Params = []
import time
import codecs

time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))



def make_report():
    page = PyH('TestReport')
    page.addCSS('static/mycss.css')
    page << meta(charset="utf-8")
    page << h2('移动端API自动化测试报告',cl='center')
    page << h5('测试完成时间：'+ time_str)
    mytable = page << div(id="div01")<<table(border="1px", cellspacing="0px") <<  tr(th('TestCaseNo') + th('TestResult') + th('TestCaseUrl',align='left') + th('TestCaseParams',align='left') + th('Response',align='left'))
    # mytab = page << table(border="1px", cellspacing="0px") << tr(th('用例编号') + th('测试结果') + th('请求接口', align='left') + th('响应数据', align='left'))
    for (i,m,n,o,k) in zip(TestCaseNo,Result,Request,Params,Response):
        if m == 'PASS':
            style = "background-color:green"
        elif m =='FAIL':
            style = "background-color:red"
        mytable<< tr(td(i) + td(m,align="center",style=style) + td(n) + td(div(o,id="div02")) + td(div(k,id="div02")))
    f = codecs.open('templates/report.html', 'w','utf-8')
    f.write(doctype)
    f.write(page.render())
    f.flush()
    f.close()