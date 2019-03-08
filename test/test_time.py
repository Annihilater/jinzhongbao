#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/23 17:45
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_time.py
import datetime


def get_month():
    date = datetime.datetime.now().date()
    date = str(date)
    month = date.replace('-', '')[:-2]  # 除去日期
    return month


if __name__ == '__main__':
    m = get_month()
    print(m)
