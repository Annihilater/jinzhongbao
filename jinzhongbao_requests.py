#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/25 21:36
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : jinzhongbao_requests.py
from config import REQUESTS_DATA, TRTM, THUUID, PICTURE_URL_PREFIX, BEGIN_DATE, URL4
from data_base.database import db
from httper.httper import HTTP
from libs import form_to_dict, get_current_month, get_months_list
from libs.bank import change
from libs.gen_time import gen_current_time
from libs.generate_begin_date import generate_begin_date
from libs.generate_encode_url_by_js_escape import generate_encode_url_by_js_escape
from libs.generate_timestamp import generate_timestamp
from libs.generate_trade_url import generate_trade_url
from libs.save_img import save_img
from models.trade import Trade


class Spider:
    def __init__(self):
        self.form_data = form_to_dict(REQUESTS_DATA)  # 抓包获得的请求查询参数
        self.begin_date = BEGIN_DATE
        self.TRTM = TRTM  # 字符串 'TRTM'
        self.THUUID = THUUID  # 字符串 'THUUID'
        self.picture_url_prefix = PICTURE_URL_PREFIX  # 小票图片链接的前缀
        self.img_path = "data/receipt/"

    def go(self):
        self.fetch_trade_data()  # 抓取文件，数据写入 MySQL
        self.down_all_pictures()  # 下载所有小票并按月份分文件夹保存

    def fetch_trade_data(self):
        session = HTTP.make_session()

        current_month = get_current_month()
        begin_date = generate_begin_date()
        month_list = get_months_list(begin_date, current_month)

        for month in month_list:
            self.get_month_trade(session, month)

        # month = get_current_month()
        # self.get_month_trade(session, month)

        # params_url = config.url4 + '?' + config.requests_data   # 将参数放在 url 中,只是介绍查询参数的请求方式，这里就不循环查了
        # response = s.post(params_url)

    def get_month_trade(self, session, month):
        """
        将抓取的月交易数据条数与数据库内对应的月份的交易数据条数进行比较，
        如果数据库数据少，则将本次抓取的月交易数据写入数据库；
        否则不写入数据库。
        """
        self.form_data["transactionDate"] = month
        str_month = str(month)[4:6]
        str_year = str(month)[:4]
        num = db.session.query(Trade).filter_by(year=str_year, month=str_month).count()

        gen_timestamp = str(generate_timestamp())
        url = URL4.replace("毫秒级时间戳", gen_timestamp)
        response = session.post(url, data=self.form_data)  # 将参数放在字典中,当做参数传递
        month_records = eval(response.text)

        newest_num = len(month_records)

        if num < newest_num:
            for item in month_records:
                self.single_record_save_to_mysql(item)
            print(str(month) + " 交易数据已成功写入数据库")
        elif num == newest_num:
            print(str(month) + " 交易数据已存在，不写入数据库")
        else:
            print(str(month) + " 数据库以保存的记录竟然比金中保服务器的数据还多？哪里出错了吧？")

    def single_record_save_to_mysql(self, item):
        """
        将单条交易记录数据的字典写入MySQL
        :param item: 单条交易记录
        """
        # 使用 Python 内部的方法拼接编码交易记录，获取交易记录详情页面 url，执行效率高
        url = generate_trade_url(item)

        # Python 内部调用 JavaScript 的方式获得交易详情页 url，效率低
        # url = generate_encode_url_by_js_escape(item)

        single_picture_url = self.picture_url_prefix + item[self.THUUID]  # 获取单个小票的链接地址

        item["create_time"] = gen_current_time()
        item["update_time"] = gen_current_time()
        item["trade_detail_url"] = url
        item["receipt_url"] = single_picture_url
        item["year"] = item["TRTM"][:4]
        item["month"] = item["TRTM"][4:6]
        item["day"] = item["TRTM"][6:8]

        try:
            if (
                not db.session.query(Trade.TRTM).filter_by(TRTM=item["TRTM"]).first()
            ):  # 查不到时，time = None
                with db.auto_commit():
                    db.session.add(Trade(**item))
                print("写入成功 ok...")
            else:
                print(item["TRTM"], "数据已存在，不写入数据")
        except Exception as e:
            print(item)

    def down_all_pictures(self):
        time_and_img_url_list = db.session.query(Trade.TRTM, Trade.receipt_url).all()
        # i = 1
        for item in time_and_img_url_list:
            time = item[0]
            month = time[:6]
            img_url = item[1]
            picture_name = time + ".png"  # 设置小票图片名称
            file_path = self.img_path + month  # 设定文件夹路径为 receipt + 月份
            save_img(img_url, picture_name, file_path)  # 按月分文件夹保存小票
            # print(i, month, time)
            # i += 1


if __name__ == "__main__":
    # db.create_db_table()
    # spider = Spider()
    # spider.fetch_trade_data()
    # spider.down_all_pictures()
    change()
