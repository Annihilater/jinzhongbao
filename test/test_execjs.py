#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/3 18:51
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_execjs.py
import execjs

print(execjs.eval('new Date'))
print(execjs.eval('Date.now()'))

