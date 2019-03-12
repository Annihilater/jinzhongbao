#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/2 22:05
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : gen_time.py
import datetime


def gen_current_time():
    now = datetime.datetime.now()
    return now


if __name__ == "__main__":
    t = gen_current_time()
    year = t.year
    month = t.month
    print(t)
    print(year)
    print(month)
