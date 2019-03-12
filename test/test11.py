#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/5 13:14
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test11.py
import datetime

text = "201901"
y = datetime.datetime.strptime(text, "%Y%m")
print(y)
print(type(y))
