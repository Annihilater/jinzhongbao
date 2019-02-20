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

from xlrd import open_workbook
from xlutils.copy import copy
from copy import deepcopy

import config
from libs import cookie_to_dict, form_to_dict, request_is_ok_or_not, write_to_file, transform_time
from libs.generate_encode_url_by_js_escape import generate_encode_url_by_js_escape
from libs.generate_trade_url import generate_trade_url
from libs.save_img import save_img
from libs.set_excel_style import set_style


class Spider:

    def __init__(self):
        self.User_Agent = config.User_Agent
        self.language = config.language
        self.Content_Type = config.Content_Type
        self.form_data = form_to_dict(config.requests_data)  # 抓包获得的请求查询参数
        self.cookies = cookie_to_dict(config.requests_cookies)  # 抓包获得的 cookie
        self.start_year = config.start_year  # 注册年份
        self.end_year = config.end_year  # 当前时间年份
        self.title_list = config.title_list
        self.TRTM = config.TRTM  # 字符串 'TRTM'
        self.THUUID = config.THUUID  # 字符串 'THUUID'
        self.transaction_date_list = config.transaction_date_list  # 从注册到当前时间的交易月份列表
        self.picture_url_prefix = config.picture_url_prefix  # 小票图片链接的前缀
        self.picture_url = []  # 票据 url 的列表
        self.tmp_month_trade = {}  # 临时存放每个月的交易记录，键: 月份，值: 当月交易记录的列表
        self.tmp_month_trade_list = []  # 临时存放每个月的交易记录，当月交易记录的列表
        self.data = []  # 抓取的交易记录列表
        self.trade_detail_url = []  # 交易记录详情页面 url 的列表

    def go(self):
        self.fetch_trade_data()  # 抓取文件，数据写入文件
        self.analysis_data()  # 从文件读取数据，处理数据，并将处理好的数据存放在 self.data 属性中
        self.down_all_pictures()  # 下载所有小票并按月份分文件夹保存
        self.write_excel()  # 将 self.data 中的数据写入 excel

    def make_session(self):
        session = requests.session()
        session.headers.update({"User-Agent": self.User_Agent, 'Content-Type': self.Content_Type})
        requests.utils.add_dict_to_cookiejar(session.cookies, cookie_dict=self.cookies)
        return session

    def fetch_trade_data(self):
        session = self.make_session()
        data = {}

        for date in self.transaction_date_list:
            self.form_data['transactionDate'] = date
            response = session.post(config.url4, data=self.form_data)  # 将参数放在字典中,当做参数传递
            data[date] = response.text

            request_is_ok_or_not(response=response, date=date)
        # params_url = config.url4 + '?' + config.requests_data   # 将参数放在 url 中,只是介绍查询参数的请求方式，这里就不循环查了
        # response = s.post(params_url)

        write_to_file(data, 'data.py')

    def analysis_data(self):
        with open('data.py', 'r') as f:
            str_data = f.read()

        # eval 函数将字符串 str 当成有效的表达式来求值并返回计算结果
        dict_data = eval(str_data)  # 将读取出的字符串数据转化为字典，字典的键为月份，字典的值为当月交易记录，值为标准的 json 对象

        for month in dict_data:
            month_trading_record = json.loads(dict_data[month])  # 取出月交易记录
            month_trading_record.reverse()  # 月交易记录本来是倒序排序，转化为正序

            for item in month_trading_record:  # item 是每条交易记录字典
                tmp_item = deepcopy(item)

                url = generate_encode_url_by_js_escape(item)  # 使用 js escape 函数编码交易记录，生成交易记录详情页面的 url
                # url = generate_trade_url(item)  # 使用 Python 内部的方法拼接编码交易记录，获取交易记录详情页面 url，很繁琐
                self.trade_detail_url.append(url)

                url_dict = {}
                single_picture_url = self.picture_url_prefix + item[self.THUUID]  # 获取单个小票的链接地址
                url_dict[item[self.TRTM]] = single_picture_url  # 以交易时间为键，将图片 url 存进字典
                self.tmp_month_trade_list.append(url_dict)  # 将单笔交易添加到月交易集合

                item[self.TRTM] = transform_time(tmp_item[self.TRTM])  # 将记录里的时间转化为正常时间
                record = list(tmp_item.values())  # 将月交易记录字典的值转化为列表
                self.data.append(record)

            self.tmp_month_trade[month] = self.tmp_month_trade_list  # 以月份为键，当月交易记录集合为值，创建月交易记录字典
            self.picture_url.append(self.tmp_month_trade)  # 将月交易记录字典存进列表
            self.tmp_month_trade_list = []  # 临时存放每个月的交易记录，用完之后清空，方便后面存放下一个月的交易记录
            self.tmp_month_trade = {}  # 临时存放每个月的交易记录，用完之后清空，方便后面存放下一个月的交易记录

    def write_excel(self):  # 写入 excel
        if not os.path.exists('trade_record.xls'):
            book = xlwt.Workbook()
            sheet1 = book.add_sheet(sheetname='trade_record', cell_overwrite_ok=True)
            for i in range(0, len(self.title_list)):
                sheet1.write(0, i, self.title_list[i], set_style('Times New Roman', 220, True))
            book.save('trade_record.xls')

        read_book = open_workbook('trade_record.xls', on_demand=True)  # 用wlrd提供的方法读取一个excel文件
        base_rows = read_book.sheets()[0].nrows  # 用wlrd提供的方法读取一个excel文件
        write_book = copy(read_book)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
        sheet1 = write_book.get_sheet(0)  # xlwt 对象的 sheet1 具有 write 权限方便后面写入数据
        for row in range(0, len(self.data)):
            for column in range(0, len(self.data[row])):
                sheet1.write(base_rows + row, column, self.data[row][column], set_style('Times New Roman', 220, True))
        write_book.save('trade_record.xls')

        print('成功写入 excel')

    def down_all_pictures(self):
        i = 1
        for month_trade in self.picture_url:
            month = list(month_trade.keys())[0]  # # 获取字典的键，因为 month_trade 字典只有一个键值对，键为月份，值为当月交易记录
            month_trade_list = month_trade[month]
            j = 1
            for trade in month_trade_list:
                picture_date = list(trade.keys())[0]  # 获取字典的键，因为 trade 字典只有一个键值对，键为日期，值为交易记录
                picture_name = picture_date + '.png'  # 设置小票图片名称
                file_path = 'receipt/' + str(month)  # 设定文件夹路径为 receipt + 月份
                save_img(trade[picture_date], picture_name, file_path)  # 按月分文件夹保存小票
                print(i, month, j, picture_date)
                i += 1
                j += 1


if __name__ == '__main__':
    spider = Spider()
    spider.go()
