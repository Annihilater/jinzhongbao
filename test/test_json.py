#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/21 14:24
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_json.py
import json

my_dict = {'img': 'hjaksdgbasjkbdnasjkn'}
my_json = json.dumps(my_dict)
print(type(my_json))
print(my_json)
