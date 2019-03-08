#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/5 13:27
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : parse_ym.py
from datetime import datetime


def parse_ym(s):
    year_s = s[0:4]
    mon_s = s[4:6]
    day_s = 1
    return datetime(int(year_s), int(mon_s), day_s)


if __name__ == '__main__':
    t = '201901'
    y_m = parse_ym(t)
    print(y_m)
