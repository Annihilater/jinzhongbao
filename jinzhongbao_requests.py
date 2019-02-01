#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/25 21:36
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : jinzhongbao_requests.py
import json
import os

import requests
import xlwt

from bs4 import BeautifulSoup
from xlrd import open_workbook
from xlutils.copy import copy

import config
from libs import cookie_to_dict, form_to_dict, request_is_ok_or_not, write_to_file, transform_time, set_style


class Spider:

    def __init__(self):
        self.User_Agent = config.User_Agent
        self.language = config.language
        self.form_data = form_to_dict(config.requests_data)
        self.cookies = cookie_to_dict(config.requests_cookies)
        self.Content_Type = config.Content_Type
        self.start_year = config.start_year
        self.end_year = config.end_year
        self.transaction_date_list = config.transaction_date_list
        self.data = []

    def fetch_trading_lists(self):
        s = requests.session()
        s.headers.update({"User-Agent": self.User_Agent, 'Content-Type': self.Content_Type})
        requests.utils.add_dict_to_cookiejar(s.cookies, cookie_dict=self.cookies)

        data = {}
        sum_url = []
        for date in self.transaction_date_list:
            self.form_data['transactionDate'] = date
            response = s.post(config.url4, data=self.form_data)   # 将参数放在字典中,当做参数传递
            response.encoding = 'utf-8'
            data[date] = response.text
            request_is_ok_or_not(response=response, date=date)
        # params_url = config.url4 + '?' + config.requests_data   # 将参数放在 url 中,只是介绍查询参数的请求方式，这里就不循环查了
        # response = s.post(params_url)
        write_to_file(data, 'data.py')
        write_to_file(sum_url, 'sum_url.py')

    @staticmethod
    def get_all_url(response_text):
        soup = BeautifulSoup(response_text, 'lxml')
        url = {}
        i = 1
        for link in soup.find_all('a'):
            print(link)
            url[i] = link
            i += 1
        return url
        # return soup.find_all('a')

    def analysis(self):
        with open('data.py', 'r') as f:
            str_data = f.read()

        dict_data = eval(str_data)  # 将读取出的字符串数据转化为字典，字典的键为月份，字典的值为当月交易记录，值为标准的 json 对象

        for i in dict_data:
            month_trading_record = json.loads(dict_data[i])  # 取出月交易记录
            month_trading_record.reverse()  # 月交易记录本来是倒序排序，转化为正序
            for item in month_trading_record:
                item['TRTM'] = transform_time(item['TRTM'])  # 将记录里的时间转化为正常时间
                record = list(item.values())  # 将月交易记录字典的值转化为列表
                self.data.append(record)

    def write_excel(self):  # 写入 excel
        if not os.path.exists('trading_record.xls'):
            book = xlwt.Workbook()
            sheet1 = book.add_sheet(sheetname='tranding_record', cell_overwrite_ok=True)
            title_list = ['时间', '商户名称', '终端序列号', '交易状态', '旧商户名', '结算金额',
                          '结算状态', 'THUUID', '交易手续费', 'RN', '交易金额', '卡号']  # 设置表格头
            for i in range(0, len(title_list)):
                sheet1.write(0, i, title_list[i], set_style('Times New Roman', 220, True))
            book.save('trading_record.xls')

        read_book = open_workbook('trading_record.xls', on_demand=True)  # 用wlrd提供的方法读取一个excel文件
        base_rows = read_book.sheets()[0].nrows     # 用wlrd提供的方法读取一个excel文件
        write_book = copy(read_book)        # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
        sheet1 = write_book.get_sheet(0)    # xlwt 对象的 sheet1 具有 write 权限方便后面写入数据
        for row in range(0, len(self.data)):
            for column in range(0, len(self.data[row])):
                sheet1.write(base_rows + row, column, self.data[row][column], set_style('Times New Roman', 220, True))
        write_book.save('trading_record.xls')

        print('成功写入 excel')

    def go(self):
        self.fetch_trading_lists()    # 抓取文件，数据写入文件
        # self.analysis()         # 从文件读取数据，处理数据，并将处理好的数据存放在 self.data 属性中
        # self.write_excel()      # 将 self.data 中的数据写入 excel


spider = Spider()
spider.go()
