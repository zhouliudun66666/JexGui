#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing


import requests


class Utils:

    # API请求地址
    Host_URL = 'http://test.coinfex.com'
    # Host_URL = 'http://192.168.0.129:8888'
    # Host_URL = 'http://api.coinfex.com'
    # Host_URL = 'http://192.168.0.195:8088'
    # Host_URL = 'http://192.168.0.135:8080'

    headers = {
            'Host': 'test.coinfex.com',
            'Connection': 'keep-alive',
            'accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.162 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN, zh;q = 0.9',
            'headerToken': ''
    }

    cookies = {
        'gr_user_id': '2baa0e60-0b98-44a1-a05e-34b438bb3322',
        'coinfex_session_id': '3ebad1c2-bcd6-404a-b820-9c4d1269d7a4thOV',
        'gr_session_id_990ee706254aaa39': '27d28af6-f91e-43f8-a0da-e7199d7c8b8e_true'
    }

    def http_get_request(self, params, url):
        response = requests.get(self.Host_URL+url, params, headers=self.headers, cookies=self.cookies ,timeout=5)
        try:
            if response.status_code == 200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpGet failed, detail is:%s,%s" % (response.text, e))
            return

    def http_post_request(self, params, url):
        response = requests.post(self.Host_URL+url, params, headers=self.headers, cookies=self.cookies,timeout=10)
        try:
            if response.status_code == 200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpPost failed, detail is:%s,%s" % (response.text, e))
            return
