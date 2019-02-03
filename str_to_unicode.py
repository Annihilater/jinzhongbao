#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/2 18:24
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : str_to_unicode.py


def to_unicode(string):
    ret = ''
    for v in string:
        ret = ret + hex(ord(v)).upper().replace('0X', '\\u')

    return ret


print(to_unicode("上海测试美容院"))
