#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/25 21:36
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : jinzhongbao_requests.py
import datetime
import json
import os

import requests
import xlwt
from http.cookies import SimpleCookie

from xlrd import open_workbook
from xlutils.copy import copy

import config


class Spider:

    def __init__(self):
        self.User_Agent = config.User_Agent
        self.language = config.language
        self.form_data = self.form_to_dict(config.requests_data)
        self.cookies = self.cookie_to_dict(config.requests_cookies)
        self.Content_Type = config.Content_Type
        self.start_year = config.start_year
        self.end_year = config.end_year
        self.transaction_date_list = config.transaction_date_list
        self.data = []

    @staticmethod
    def transform_time(time_str):
        new_time = datetime.datetime.strptime(time_str, "%Y%m%d%H%M%S")
        new_time = str(new_time)
        return new_time

    @staticmethod
    def cookie_to_dict(raw):
        cookie = SimpleCookie(raw)
        dict_cookies = {i.key: i.value for i in cookie.values()}
        return dict_cookies

    @staticmethod
    def dict_to_json(raw):
        json_cookies = json.dumps(raw)
        return json_cookies

    @staticmethod
    def form_to_dict(raw):
        tmp_list = raw.split('&')
        tmp_dict = {}

        for i in tmp_list:
            tmp = i.split('=')
            tmp_dict[tmp[0]] = tmp[1]

        return tmp_dict

    @staticmethod
    def set_style(name, height, bold=False):  # 设置表格样式
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style

    def transaction_date(self):
        transaction_date_list = []
        year = list(range(self.start_year, self.end_year + 1))
        month = list(range(1, 13))

        for x in range(0, len(year)):
            for y in range(0, len(month)):
                str_year = str(year[x])  # 将数字年转为字符串
                str_month = str(month[y])  # 将数字月转为字符串
                str_month = '0' + str_month if len(str_month) == 1 else str_month  # 单位数月份前面加 '0'
                transaction_date = int(str_year + str_month)
                transaction_date_list.append(transaction_date)

        return transaction_date_list

    def fetch_content(self):
        s = requests.session()
        s.headers.update({"User-Agent": self.User_Agent, 'Content-Type': self.Content_Type})
        requests.utils.add_dict_to_cookiejar(s.cookies, cookie_dict=self.cookies)

        data = {}
        for date in self.transaction_date_list:
            self.form_data['transactionDate'] = date
            response = s.post(config.url4, data=self.form_data)
            data[date] = response.text

        with open('data.py', 'w') as f:  # 将抓取的数据写入文件保存
            f.write(str(data))

    def analysis(self):
        with open('data.py', 'r') as f:
            str_data = f.read()

        dict_data = eval(str_data)  # 将读取出的字符串数据转化为字典，字典的键为月份，字典的值为当月交易记录，值为标准的 json 对象

        for i in dict_data:
            month_trading_record = json.loads(dict_data[i])  # 取出月交易记录
            month_trading_record.reverse()  # 月交易记录本来是倒序排序，转化为正序
            for item in month_trading_record:
                item['TRTM'] = self.transform_time(item['TRTM'])  # 将记录里的时间转化为正常时间
                record = list(item.values())  # 将月交易记录字典的值转化为列表
                self.data.append(record)

    def write_excel(self):  # 写入 excel
        if not os.path.exists('trading_record.xls'):
            book = xlwt.Workbook()
            sheet1 = book.add_sheet(sheetname='tranding_record', cell_overwrite_ok=True)
            title_list = ['时间', '商户名称', '终端序列号', '交易状态', '旧商户名', '结算金额',
                          '结算状态', 'THUUID', '交易手续费', 'RN', '交易金额', '卡号']  # 设置表格头
            for i in range(0, len(title_list)):
                sheet1.write(0, i, title_list[i], self.set_style('Times New Roman', 220, True))
            book.save('trading_record.xls')

        read_book = open_workbook('trading_record.xls', on_demand=True)  # 用wlrd提供的方法读取一个excel文件
        base_rows = read_book.sheets()[0].nrows     # 用wlrd提供的方法读取一个excel文件
        write_book = copy(read_book)        # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
        sheet1 = write_book.get_sheet(0)    # xlwt 对象的 sheet1 具有 write 权限方便后面写入数据
        for row in range(0, len(self.data)):
            for column in range(0, len(self.data[row])):
                sheet1.write(base_rows + row, column, self.data[row][column], self.set_style('Times New Roman', 220, True))
        write_book.save('trading_record.xls')

    def go(self):
        self.fetch_content()    # 抓取文件，数据写入文件
        self.analysis()         # 从文件读取数据，处理数据，并将处理好的数据存放在 self.data 属性中
        self.write_excel()      # 将 self.data 中的数据写入 excel


spider = Spider()
spider.go()
