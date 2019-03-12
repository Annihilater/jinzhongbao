#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/3 01:35
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : gen_big_data.py
import re

from config import PATH1, PATH2, PATH3, PATH_LIST, ACQUIRER_PATH, AREA_PATH
from libs.acquirer import get_acquirer_data
from libs.area import get_area_data
from libs.gen_time import gen_current_time
from libs.parse_ym import parse_ym


def gen_big_data(path, acquirer_path, area_path):
    """
    生成招行天书数据
    :param path: '/user/down/201901.txt'
    :param acquirer_path: '/user/down/收单机构码.txt'
    :param area_path: '/user/down/全国地区码.txt'
    :return: 201901 的黑名单列表 [{...}, {...}, {...}, {...}, ...]
    """
    acquirer_data = get_acquirer_data(acquirer_path)

    area = get_area_data(area_path)
    area_data = area.get_area_data()

    file_name = path.split("/")[-1]
    with open(path, "r") as f:
        lines = f.readlines()  # 一次性读取一个天书文件的内容

    data = []
    lines = set(lines)
    for line in lines:
        try:
            r = re.findall("(.*)[,\n](.*)[\n]", line)[0]
            item = dict()
            item["create_time"] = gen_current_time()
            item["cmb_update_time"] = parse_ym(file_name)
            item["merc_num"] = r[0]
            item["merc_name"] = r[1]

            acquirer_num = item["merc_num"][:3]
            if acquirer_num in acquirer_data:
                item["acquirer_num"] = acquirer_num
                item["acquirer_name"] = acquirer_data[acquirer_num]
            else:
                item["acquirer_num"] = ""
                item["acquirer_name"] = ""

            item["mcc"] = item["merc_num"][7:11]

            area_num = item["merc_num"][3:7]
            if area_num in area_data:
                item["area_num"] = area_num
                item["area_name"] = area_data[area_num]
            else:
                item["area_num"] = ""
                item["area_name"] = ""

            item["merc_seq_num"] = item["merc_num"][11:15]
            item["cmb_jf"] = 0

            r = (
                item["create_time"],
                item["cmb_update_time"],
                item["merc_num"],
                item["merc_name"],
                item["acquirer_num"],
                item["acquirer_name"],
                item["mcc"],
                item["area_num"],
                item["area_name"],
                item["merc_seq_num"],
                item["cmb_jf"],
            )
            data.append(r)

        except Exception as e:
            print(line, "哪里出错了？")
            print(e)
            continue

    return data


if __name__ == "__main__":
    path1, path2, path3 = PATH1, ACQUIRER_PATH, AREA_PATH
    my_data = gen_big_data(path1, path2, path3)
    print(len(my_data))
