#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/3 19:18
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : generate_encode_url_by_js_escape.py
import execjs

import config


def generate_encode_url_by_js_escape(trade_data):
    """
    通过 execjs 实现在 Python 内部调用 JavaScript 的 escape 函数为交易记录编码，最后生成交易记录详情页面的 url
    :param trade_data:
    :return:
    """
    data = str(trade_data)
    trade_url_prefix = config.TRADE_URL_PREFIX

    ctx = execjs.compile("""
        function encode_trade_data(data){
            return escape(data)
        }
    """)

    encode_url = ctx.call("encode_trade_data", data)
    encode_url = trade_url_prefix + encode_url
    return encode_url
