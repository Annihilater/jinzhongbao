#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/3 18:55
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_js_escape.py
import execjs

from config import trade_data, TRADE_URL_PREFIX


def generate_encode_url_by_js_escape(raw):
    data = str(raw)
    trade_url_prefix = TRADE_URL_PREFIX

    ctx = execjs.compile("""
        function encode_trade_data(data){
            return escape(data)
        }
    """)

    encode_url = ctx.call("encode_trade_data", data)
    encode_url = trade_url_prefix + encode_url
    return encode_url


if __name__ == '__main__':
    test_trade_data = trade_data
    my_encode_url = generate_encode_url_by_js_escape(test_trade_data)
    print(my_encode_url)
