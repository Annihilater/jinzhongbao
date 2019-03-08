#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/23 18:21
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_date.py
import datetime


def get_months_list(begin, end):
    start_date = datetime.datetime.strptime(begin, '%Y%m')
    end_date = datetime.datetime.strptime(end, '%Y%m')
    dates = []
    dt = start_date  # dt 为日期类型
    while dt <= end_date:
        dt = int(datetime.datetime.strftime(dt, '%Y%m'))  # 将 dt 由日期类型转换为字符串类型，再转换为数字类型
        dates.append(dt)
        dt = str(dt)  # 将 dt 由数字类型转换为字符串类型
        dt = datetime.datetime.strptime(dt, '%Y%m')  # 将 dt 由字符串转换为日期类型
        dt = dt + datetime.timedelta(days=31)  # dt 增加一个月的时间间隔

    return dates


if __name__ == '__main__':
    begin_date_str = '201808'
    end_date_str = '202001'
    date_list = get_months_list(begin_date_str, end_date_str)
    print(date_list)
