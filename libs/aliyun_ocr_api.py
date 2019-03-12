#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/4 11:09
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : aliyun_ocr_api.py
import base64
import json
import os
import time
import urllib.request
import urllib.parse
import urllib.error

from config import aliyun_ocr_api_url, Authorization


def aliyun_ocr_api(img_path, output_path):
    if os.path.exists(output_path):
        print("ocr 识别数据已存在，不调用 api")
        return
    with open(img_path, "rb") as f:  # 以二进制读取本地图片
        data = f.read()
        encode_str = str(base64.b64encode(data), "utf-8")

    img = {"img": encode_str}
    url_request = aliyun_ocr_api_url

    # 请求头
    headers = {
        "Authorization": Authorization,
        "Content-Type": "application/json; charset=UTF-8",
    }

    response = post_url(url_request, img_dict=img, headers=headers)
    with open(output_path, "a") as f:
        f.write(response)
        f.write("\n")

    print("ocr 完成，数据已全部写入到", output_path)


def post_url(url, img_dict, headers):  # 调用阿里云 ocr 服务发送 post 请求
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
