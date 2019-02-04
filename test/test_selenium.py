#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/4 10:41
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_selenium.py
from selenium import webdriver
import time

from config import chromedriver_path

browser = webdriver.Chrome(chromedriver_path)

browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
sreach_window = browser.current_window_handle

browser.find_element_by_xpath('//*[@id="2"]/h3/a').click()
time.sleep(5)
