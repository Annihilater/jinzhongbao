#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/26 11:44
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : time_trans.py
# 时间格式转换，时间的所有数字当做字符叠加在一起的字符串转化为正常时间
import datetime

time_str = '20190102111747'
time = datetime.datetime.strptime(time_str, "%Y%m%d%H%M%S")
time = str(time)
print(time)
