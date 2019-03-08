#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/2 21:49
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_re_1.py
import re

line1 = '833392156410016,\n'
line2 = '104310059120067,上海第一医药川沙大药房有限公司\n'
k = [line1, line2]

for i in k:
    r = re.findall('(.*)[,\n](.*)[\n]', i)[0]
    print(r)
    merc_num = r[0]
    merc_name = r[1]
    print(merc_num, merc_name)
    print('--------------------------------')
