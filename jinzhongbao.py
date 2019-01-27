#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/24 10:23
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : jinzhongbao.py
# 本文件没有写完，因为写到中途发现了更好的方法所以放弃了

import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config


class Spider:
    url = config.url
    fake_url = config.fake_url
    User_Agent = config.User_Agent
    language = config.language
    cookies = config.cookies
    chrome_driver = config.chromedriver_path

    root_pattern = config.root_pattern
    merchant_order_name_pattern = config.merchant_order_name_pattern
    amount_pattern = config.amount_pattern

    def go(self):
        html = self.__fetch__content()
        html = self.__analysis(html)
        with open('content.html', 'w') as f:
            f.write(str(html))

    def __fetch__content(self):
        opts = Options()
        opts.add_argument("user-agent={}".format(self.User_Agent))
        opts.add_argument("language={}".format(self.language))

        browser = webdriver.Chrome(self.chrome_driver, chrome_options=opts)
        browser.set_window_size(500, 900)
        browser.set_window_position(1300, 10)
        # new_user_agent = browser.execute_script("return navigator.userAgent;")
        # new_language = browser.execute_script("return navigator.language;")
        # print(new_user_agent)
        # print(new_language)
        browser.get(self.fake_url)
        print('current_url:', browser.current_url)

        for cookie in self.cookies:
            browser.add_cookie(cookie_dict=cookie)

        browser.get(self.url)
        page_source = browser.page_source
        return page_source

    def __analysis(self, html):
        root_html = re.findall(self.root_pattern, html, re.S)

        # trans = {}
        # for item in root_html:
        #     trans['商户名称'] = re.findall(self.name_pattern, item, re.S)
        #     trans['交易金额'] = re.findall(self.name_pattern, item, re.S)
        #     trans['交易状态'] = re.findall(self.name_pattern, item, re.S)
        #     trans['交易时间'] = re.findall(self.name_pattern, item, re.S)
        return root_html

    def __refine(self):
        pass


spider = Spider()
spider.go()
