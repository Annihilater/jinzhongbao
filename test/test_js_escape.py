#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/3 18:55
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_js_escape.py
import execjs

import config

test_trade_data = config.trade_data


def generate_encode_url_by_js_escape(trade_data):
    data = str(trade_data)
    trade_url_prefix = config.trade_url_prefix

    ctx = execjs.compile("""
        function encode_trade_data(data){
            return escape(data)
        }
    """)

    encode_url = ctx.call("encode_trade_data", data)
    encode_url = trade_url_prefix + encode_url
    return encode_url


my_encode_url = generate_encode_url_by_js_escape(test_trade_data)
print(my_encode_url)
