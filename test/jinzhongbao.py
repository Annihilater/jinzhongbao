#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/24 10:23
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : jinzhongbao.py
# 本文件没有写完，因为写到中途发现了更好的方法所以放弃了

import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import (
    URL,
    FAKE_URL,
    USER_AGENT,
    LANGUAGE,
    CHROMEDRIVER_PATH,
    root_pattern,
    merchant_order_name_pattern,
    amount_pattern,
    COOKIES,
)


class Spider:
    def __init__(self):
        self.url = URL
        self.fake_url = FAKE_URL
        self.User_Agent = USER_AGENT
        self.language = LANGUAGE
        self.cookies = COOKIES
        self.chrome_driver = CHROMEDRIVER_PATH

        self.root_pattern = root_pattern
        self.merchant_order_name_pattern = merchant_order_name_pattern
        self.amount_pattern = amount_pattern

        self.picture_url = []
        self.picture_single_url_dict = {}

    def go(self):
        self.__fetch__content()
        # html = self.__analysis(html)
        # with open('content.html', 'w') as f:
        #     f.write(str(html))

    def __fetch__content(self):
        opts = Options()
        opts.add_argument("user-agent={}".format(self.User_Agent))
        opts.add_argument("language={}".format(self.language))

        driver = webdriver.Chrome(self.chrome_driver, chrome_options=opts)
        # driver.set_window_size(500, 900)
        # driver.set_window_position(1300, 10)
        # new_user_agent = driver.execute_script("return navigator.userAgent;")
        # new_language = driver.execute_script("return navigator.language;")
        # print(new_user_agent)
        # print(new_language)
        driver.get(self.fake_url)
        print("current_url:", driver.current_url)

        for cookie in self.cookies:
            driver.add_cookie(cookie_dict=cookie)

        try:
            for i in range(2, 12):
                driver.get(self.url)

                trade_time_xpath = (
                    '//*[@id="container"]/div/div[2]/div[3]/div['
                    + str(i)
                    + "]/div/a/div/p[5]"
                )
                trade_detail_xpath = (
                    '//*[@id="container"]/div/div[2]/div[3]/div[' + str(i) + "]/div"
                )
                trade_time = driver.find_element_by_xpath(trade_time_xpath).text
                driver.find_element_by_xpath(trade_detail_xpath).click()
                # time.sleep(1)
                driver.implicitly_wait(1)

                driver.find_element_by_xpath('//*[@id="dzpd"]/a').click()
                picture_url = driver.current_url
                self.picture_single_url_dict[trade_time] = picture_url
                self.picture_url.append(self.picture_single_url_dict)
                self.picture_single_url_dict = {}

            # driver.get(self.url)
            # trade_info_list = driver.find_elements_by_css_selector('.weui-cell__bd')
            # for trade_info_web_element in trade_info_list:
            #     trade_info = trade_info_web_element.text
            #     trade_time = trade_info.split('\n')[4]
            #
            #     driver.find_element_by_class_name('weui-cell').click()
            #     driver.implicitly_wait(1)
            #
            #     driver.find_element_by_xpath('//*[@id="dzpd"]/a').click()
            #
            #     picture_url = driver.current_url
            #     self.picture_single_url_dict[trade_time] = picture_url
            #     self.picture_url.append(self.picture_single_url_dict)
            #     self.picture_single_url_dict = {}
            #     driver.back()
            #
            # time.sleep(5)
            # driver.close()
            a = 1
        except Exception as e:
            print(e)
        finally:
            driver.close()

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
