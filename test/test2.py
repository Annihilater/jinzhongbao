#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/24 09:29
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test2.py


import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from config import chromedriver_path

service = service.Service(chromedriver_path)
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml')
time.sleep(5)  # Let the user actually see something!
driver.quit()
