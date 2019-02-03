#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/2 17:38
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test9.py
from urllib.parse import unquote, quote
from config import encode_str2

encode_str = encode_str2

decode_str = unquote(encode_str)
print(decode_str)

new_encode_str = quote(decode_str)
print(encode_str)
print(new_encode_str)


if new_encode_str == encode_str:
    print('=')
else:
    print('!=')
