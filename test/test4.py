#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/27 00:21
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test4.py
# 判断当前目录下的问价内存不存在
import os

if os.path.exists("test5.py"):
    print("存在")
else:
    print("不存在")
