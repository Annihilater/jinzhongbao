#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/4 13:29
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_re.py
import re


def convert(value):
    # 将匹配的字符串从 value 里面取出来
    matched = value.group()
    # print(value, type(value))
    return '+'


my_str = '商户名称：上海白玉兰美容院\n交易金额：2117\n交易状态：成功\n结算状态：结算成功\n2019-01-28 21:09:01'

# my_str = re.sub('\n', convert, my_str)
# print(my_str)
# my_str = my_str.split('+')
# print(my_str)
# print(my_str[4])
my_str = my_str.split('\n')[4]
print(my_str)

