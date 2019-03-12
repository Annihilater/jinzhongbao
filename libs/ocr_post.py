#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/22 15:34
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : ocr_post.py
import urllib.request
import urllib.parse
import urllib.error
import json
import time


# 调用阿里云 ocr 服务发送 post 请求
def post_url(url, img_dict, headers):
    try:
        params = json.dumps(img_dict).encode(encoding="UTF8")
        req = urllib.request.Request(url, params, headers)
        r = urllib.request.urlopen(req)
        html = r.read()
        r.close()
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    time.sleep(1)
