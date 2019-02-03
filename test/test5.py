#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/27 01:03
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test5.py
# 字典的列表的字符串类型 转化为 字典的列表类型
import json

s = '[{"a": 1, "b": 2, "c": 3}]'
print(type(s))

s = json.loads(s)
print(type(s))
print(s)
for item in s:
    print(type(item), item)
