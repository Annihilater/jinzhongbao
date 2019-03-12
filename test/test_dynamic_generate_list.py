#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/3 09:51
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_dynamic_generate_list.py


# for i in range(4):
#     name = 'v' + str(i)
#     locals()['v' + str(i)] = i
month = 201808

str_month = "month"
a = globals()[str_month]

L = list(str_month)
print(L)
