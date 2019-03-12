#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/2 18:04
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test10.py

s = "测试美容院"
s_unicode = u"测试美容院"
s_gb2312 = s.encode("gb2312")
s_uft_8 = s.encode("utf-8")
print(type(s))
print(s)

print(type(s_unicode))
print(s_unicode)

print(type(s_gb2312))
print(s_gb2312)

print(type(s_uft_8))
print(s_uft_8)
