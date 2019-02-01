#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/1 13:10
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : __init__.py.py
import datetime
import json
from http.cookies import SimpleCookie

import xlwt


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


def set_style(name, height, bold=False):  # 设置表格样式
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


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
            str_month = '0' + str_month if len(str_month) == 1 else str_month  # 单位数月份前面加 '0'
            transaction_date_num = int(str_year + str_month)
            transaction_date_list.append(transaction_date_num)

    return transaction_date_list








