#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/3 11:28
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : generate_trade_url.py
import json
import re
from copy import deepcopy
from urllib.parse import quote

import config


def generate_trade_url(item):
    record_dict = deepcopy(item)
    # 生成交易记录详情页面的 url
    trade_url_prefix = config.TRADE_URL_PREFIX

    def to_unicode(string):
        # 将中文转化为 unicode
        ret = ''
        for v in string:
            ret = ret + hex(ord(v)).upper().replace('0X', '\\u')
            # ord 函数会返回字符的 ascii 数值、unicode 数值
            # upper 函数将返回的数值里的字母转为大写
            # replace 函数将返回的十六进制前缀 '0X' 替换为 '\u'
            # '\\u' 第一个'\'是为了转义第二个'\'
        return ret

    def trans_merchant_order_name(the_record_dict):
        # 从字典中取出 MERCHANT_ORDER_NAME 转为 unicode，并提前拼接好
        merchant_order_name = to_unicode(the_record_dict['MERCHANT_ORDER_NAME'])
        merchant_order_name = merchant_order_name.replace('\\', '%')
        tmp_merchant_order_name_unicode = 'MERCHANT_ORDER_NAME%22%3A%22' + merchant_order_name + '%22%2C%22'
        return tmp_merchant_order_name_unicode

    def trans_js_status(the_record_dict):
        # 从字典中取出 JSSTATUS 转为 unicode，并提前拼接好
        js_status = to_unicode(the_record_dict['JSSTATUS'])
        js_status = js_status.replace('\\', '%')
        tmp_js_status_unicode = 'JSSTATUS%22%3A%22' + js_status + '%22%2C%22'
        return tmp_js_status_unicode

    def convert_merchant_order_name(value):
        # 将匹配的字符串从 value 里面取出来
        matched = value.group()
        return merchant_order_name_unicode + matched

    def convert_js_status(value):
        # 将匹配的字符串从 value 里面取出来
        matched = value.group()
        return js_status_unicode + matched

    merchant_order_name_unicode = trans_merchant_order_name(record_dict)
    js_status_unicode = trans_js_status(record_dict)

    record_dict.pop("MERCHANT_ORDER_NAME")  # 从字典中删除 MERCHANT_ORDER_NAME
    record_dict.pop("JSSTATUS")             # 从字典中删除 JSSTATUS

    json_trading_record = json.dumps(record_dict)   # 将除去 MERCHANT_ORDER_NAME、JSSTATUS 之后的字典转为 json 对象
    encode_trading_record = quote(json_trading_record)     # 将 json 对象解码

    # 因为 json 对象中的不需要解码的空格和星号替换回来
    encode_trading_record = re.sub('%2A%2A%2A%2A', '****', encode_trading_record, 1)
    encode_trading_record = re.sub('%20', '', encode_trading_record)

    # 将之前除去的 MERCHANT_ORDER_NAME、JSSTATUS 拼接回来
    encode_trading_record = re.sub('SEQNO', convert_merchant_order_name, encode_trading_record, 1)
    encode_trading_record = re.sub('THUUID', convert_js_status, encode_trading_record, 1)
    # print(baiyulan_correct_encode)
    # print(encode_trading_record)
    # if encode_trading_record == baiyulan_correct_encode:
    #     print('=')
    # else:
    #     print('!=')

    url = trade_url_prefix + encode_trading_record
    return url


if __name__ == '__main__':
    dict_trading_record = {}
    trade_detail_url = generate_trade_url(dict_trading_record)
    print(trade_detail_url)
