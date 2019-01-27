#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/27 01:13
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test6.py
# 遍历字典的键
s = {'a': 1, 'b': 2, 'c': 3}
for key in s:
    print(s[key])

# 以元组、字典、集合的元素为键创建字典，字典的所有值都为 None
a = ('d', 'e', 'f')  # 元组
x = {'d', 'e', 'f'}  # 集合
y = ['d', 'e', 'f']  # 列表
print(s.keys())
print(s.fromkeys(a))
print(s.fromkeys(x))
print(s.fromkeys(y))
