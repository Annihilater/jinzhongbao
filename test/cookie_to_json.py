#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/31 18:01
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : cookie_to_json.py
import json

import config

cookies = config.requests_cookies


def cookie_to_json(raw):
    tmp_list = raw.split(";")
    tmp_dict = {}

    for i in tmp_list:
        i = i[1:]
        tmp = i.split("=")
        tmp_dict[tmp[0]] = tmp[1]

    json_cookies = json.dumps(tmp_dict)
    return json_cookies


my_json_cookies = cookie_to_json(cookies)
print(my_json_cookies)
