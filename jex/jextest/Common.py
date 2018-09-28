#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import re
import base64
import hashlib
import hmac
import time
import datetime
import random
import MyException

teleNum = random.choice(['150', '137', '189']) + ''.join(random.choice('0123456789') for i in range(8))
email = ''.join(random.choice('123456789') for i in range(9)) + '@qq.com'

# 123456
pwdOne = 'GIsPp%2Btfp8WoMX40pkIRceEXnACxi34IU3x9RkZZjnOdBHHr0hRREdZvQXMgpXrQ%2F' \
         'CQf8nOTEgC98sgeMRAFK%2Fvq9fCy1cMboC1%2FpLbmISYAtV6%2FG%2FPsviJ3oW5mQ9' \
         '73eUqHZ%2B%2ByTIQZT%2FiFzWR7w0DBBHz%2BAicglyL2e5NcGYwfB3mHsTWtq3%2F8Z' \
         'PcVmWRHDXFULN6lczFjGsRzt%2BwcrwGU2E6ZO6fs%2F3LhagUKRNWs7Tt0HS0KQRJ9M77' \
         '4dHJ7xEhnp0N9D7PZyRtbuJN1SYpbuzcngmGYWygkIhxGfzn61TMZkC5bk5o9GM32oV4v' \
         '2WZLNNCegC1Yz7yxEiDJPQ%3D%3D'

# 111111
pwdTwo = 'fgRbnc6hfnutOtT6soub3aSNGLOJCMHbiYsPR7mZZXoH0UkMFzzJ0P6EXH1ssxw9w%2Fee' \
         'J%2Bvmriv%2FKpK2Hm%2BGJphqnU5zNdytePgRoDhnbxc31brPDqT0Tm3JC67Jk7aA%2Bl' \
         '0s288nEEfDt5OCtbjEeEz2ebbCodv9x%2BOjYmBdWPZBAEt75AFHbLIQYoWKQIt5K%2BpO' \
         'reVlLj%2F7qW0lgMQsjfmDOws%2F9N5va%2Bpd2%2B83c4nxv4TxXbkDyEKveeHMTnPihH' \
         '2uPKejGk6jKuoXHT2S9YEudd6dHs%2BFZuCFeEoBryuPxRkuj4sz4OcUWDfYQoizM3c9nGh' \
         '2dM14z1Ude5FKhg%3D%3D'


def get_ali():
    f = open("./aliyun.txt", 'r')
    ali_list = f.readlines()
    f.close()
    return ali_list


Aliyun_list = get_ali()


def search_str(response, regex_list):
    try:
        for i in regex_list:
            re_com = re.compile(i)
            search_str = re_com.search(response)
            if search_str is None:
                raise MyException.NotMatchException("未匹配到预期结果")
                return False
    except Exception as e:
        print("Failed, response is : %s,%s" % (response, e))
        raise e


def byte_secret(secret):
    missing_padding = len(secret) % 8
    if missing_padding != 0:
        secret += '=' * (8 - missing_padding)
    return base64.b32decode(secret, casefold=True)


def int_to_bytestring(i, padding=8):
    result = bytearray()
    while i != 0:
        result.append(i & 0xFF)
        i >>= 8
    return bytes(bytearray(reversed(result)).rjust(padding, b'\0'))


def generate_otp(secret):
    for_time = datetime.datetime.now()
    i = time.mktime(for_time.timetuple())
    input = int(i / 30)
    digest = hashlib.sha1
    digits = 6
    if input < 0:
        raise ValueError('input must be positive integer')
    hasher = hmac.new(byte_secret(secret), int_to_bytestring(input), digest)
    hmac_hash = bytearray(hasher.digest())
    offset = hmac_hash[-1] & 0xf
    code = ((hmac_hash[offset] & 0x7f) << 24 |
            (hmac_hash[offset + 1] & 0xff) << 16 |
            (hmac_hash[offset + 2] & 0xff) << 8 |
            (hmac_hash[offset + 3] & 0xff))
    str_code = str(code % 10 ** digits)
    while len(str_code) < digits:
        str_code = '0' + str_code
    return str_code
