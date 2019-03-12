#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/5 13:47
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : get_jg_num.py
import os

from config import ACQUIRER_PATH, FOLDER_PATH
from data_base.database import db
from libs.gen_time import gen_current_time
from libs.switch_ac_type import switch_ac_type
from models.acquirer import Acquirer


def get_acquirer_data(p):
    """
    :param p: 收单机构代码文件路径
    :return:
    """
    file_name = p.split("/")[-1]
    ac_type = switch_ac_type(file_name)

    with open(p, "r") as f:
        lines = f.readlines()

    data = []
    for line in lines:
        r = line.split("\t")
        if r[0] != "机构号":
            ac_code = r[0]
            area_code = r[1].replace("\n", "")
            ac_name = r[2].replace("\n", "")

            d = dict()
            d["create_time"] = gen_current_time()
            d["update_time"] = gen_current_time()
            d["ac_type"] = ac_type
            d["ac_code"] = ac_code
            d["area_code"] = area_code
            d["ac_name"] = ac_name
            data.append(d)

    return data


if __name__ == "__main__":
    db.create_db_table()
    # path = ACQUIRER_PATH
    folder_path = FOLDER_PATH
    file_list = list(os.walk(folder_path))[0][2]
    for file in file_list:
        path = folder_path + file
        result = get_acquirer_data(path)

        for item in result:
            with db.auto_commit():
                db.session.add(Acquirer(**item))
