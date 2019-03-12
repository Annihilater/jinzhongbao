#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/24 09:09
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test.py


import time
from selenium import webdriver
from config import CHROMEDRIVER_PATH

driver = webdriver.Chrome(CHROMEDRIVER_PATH)
# Optional argument, if not specified will search path.

driver.get("http://www.google.com/xhtml")
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name("q")
search_box.send_keys("ChromeDriver")
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()
