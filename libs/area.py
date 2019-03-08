#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/5 14:21
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : area.py
from config import AREA_PATH
from data_base.database import db
from libs.gen_time import gen_current_time
from models.area import Area


def get_area_data(path):
    data = []
    with open(path, 'r') as f:
        lines = f.readlines()

    province_name = ''
    for line in lines:
        d = dict()
        r = line.split('\t')
        if len(r) == 1:
            province_name = r[0].replace('\n', '')
            continue
        try:
            area_num = r[0]
            area_name = r[1].replace('\n', '')

            d['create_time'] = gen_current_time()
            d['update_time'] = gen_current_time()
            d['area_code'] = area_num
            d['province_name'] = province_name
            d['area_name'] = area_name
            data.append(d)
        except Exception as e:
            print('哪里出问题了？')
            print(e)
    return data


if __name__ == '__main__':
    db.create_db_table()
    area_path = AREA_PATH
    my_data = get_area_data(area_path)

    for item in my_data:
        with db.auto_commit():
            db.session.add(Area(**item))
