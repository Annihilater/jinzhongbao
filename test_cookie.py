#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/25 22:02
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_cookie.py
# requests 库使用 RequestsCookieJar 对象设置 cookie，这在设置多条 cookie(每条 cookie 是一个字典的时候) 的时候比较有用
# 是相区别于每条 cookie 作为键值对，多条 cookie 存放在一个字典中的时候比较有用
# 暂时不清楚这两种方式的 cookie 有什么区别
import requests
from requests.cookies import RequestsCookieJar

jar = RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)
print(r.status_code)
