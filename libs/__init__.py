#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/1 13:10
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : __init__.py.py
import datetime
import json
from http.cookies import SimpleCookie


def transform_time(time_str):
    new_time = datetime.datetime.strptime(time_str, "%Y%m%d%H%M%S")
    new_time = str(new_time)
    return new_time


def cookie_to_dict(raw):
    cookie = SimpleCookie(raw)
    dict_cookies = {i.key: i.value for i in cookie.values()}
    return dict_cookies


def dict_to_json(raw):
    json_cookies = json.dumps(raw)
    return json_cookies


def form_to_dict(raw):
    tmp_list = raw.split('&')
    tmp_dict = {}

    for i in tmp_list:
        tmp = i.split('=')
        tmp_dict[tmp[0]] = tmp[1]

    return tmp_dict


def request_is_ok_or_not(response, date):
    if response.status_code == 200:
        print(date, '请求成功')
    else:
        print(date, '请求失败')


def write_to_file(raw, file_name):
    with open(file_name, 'w') as f:
        f.write(str(raw))


def transaction_date(start_year, end_year):
    transaction_date_list = []
    year = list(range(start_year, end_year + 1))
    month = list(range(1, 13))

    for x in range(0, len(year)):
        for y in range(0, len(month)):
            str_year = str(year[x])  # 将数字年转为字符串
            str_month = str(month[y])  # 将数字月转为字符串
            str_month = '0' + \
                str_month if len(str_month) == 1 else str_month  # 单位数月份前面加 '0'
            transaction_date_num = int(str_year + str_month)
            transaction_date_list.append(transaction_date_num)

    return transaction_date_list


def get_word(dic_t):
    return dic_t['word']


def get_current_month():
    date = datetime.datetime.now().date()
    date = str(date)
    month = date.replace('-', '')[:-2]  # 除去日期
    return month


def get_months_list(begin, end):
    start_date = datetime.datetime.strptime(str(begin), '%Y%m')
    end_date = datetime.datetime.strptime(str(end), '%Y%m')
    dates = []
    dt = start_date  # dt 为日期类型
    while dt <= end_date:
        # 将 dt 由日期类型转换为字符串类型，再转换为数字类型
        dt = int(datetime.datetime.strftime(dt, '%Y%m'))
        dates.append(dt)
        dt = datetime.datetime.strptime(
            str(dt), '%Y%m')  # 将 dt 由数字类型转换为字符串类型, 再转换为日期类型
        dt = dt + datetime.timedelta(days=31)  # dt 增加一个月的时间间隔

    dates.append(int(datetime.datetime.strftime(end_date, '%Y%m')))
    return dates
