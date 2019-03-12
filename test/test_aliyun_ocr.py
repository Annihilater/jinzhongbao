#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/21 13:24
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_aliyun_ocr.py

# python3
import base64

from config import image_file, Authorization, aliyun_ocr_api_url
from libs import get_word
from libs.aliyun_ocr_api import post_url


def ocr_extract_data():
    with open(image_file, 'rb') as f:  # 以二进制读取本地图片
        data = f.read()
        encode_str = str(base64.b64encode(data), 'utf-8')
    # 请求头
    headers = {
        'Authorization': Authorization,
        'Content-Type': 'application/json; charset=UTF-8'
    }

    url_request = aliyun_ocr_api_url
    img = {'img': encode_str}

    my_html = post_url(url_request, img_dict=img, headers=headers)
    with open('aliyun_ocr.txt', 'w') as f:
        f.write(my_html)
    print('my_html:', my_html)

    sum_receipt = []
    single_receipt = {}
    with open('aliyun_ocr.txt', 'r') as f:
        ocr_data = f.read()
    ocr_data = eval(ocr_data)
    ocr_data = ocr_data["prism_wordsInfo"]
    single_receipt['商户名称'] = get_word(ocr_data[5])
    single_receipt['商户编号'] = get_word(ocr_data[7])
    single_receipt['终端号'] = get_word(ocr_data[10])
    single_receipt['操作员'] = get_word(ocr_data[11])
    single_receipt['发卡行'] = get_word(ocr_data[14])
    single_receipt['收单行'] = get_word(ocr_data[16])
    single_receipt['银行卡号'] = get_word(ocr_data[18]).replace('/C', '')
    single_receipt['批次号'] = get_word(ocr_data[21])
    single_receipt['凭证号'] = get_word(ocr_data[22])
    single_receipt['交易时间'] = get_word(ocr_data[25]).replace(
        '/', '') + get_word(ocr_data[26]).replace('：', '')
    single_receipt['检索参考号'] = get_word(ocr_data[29])
    single_receipt['授权码'] = get_word(ocr_data[30])
    single_receipt['金额'] = get_word(ocr_data[33])

    sum_receipt.append(single_receipt)
    print(single_receipt)

    i = 0
    for item in ocr_data:
        del item['pos']
        print(i, item)
        i += 1


if __name__ == "__main__":
    ocr_extract_data()
