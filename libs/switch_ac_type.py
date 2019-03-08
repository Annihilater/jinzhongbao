#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/6 13:02
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : switch_ac_type.py


def switch_ac_type(file_name):
    if file_name == '全国247家商业银行收单机构号.txt':
        ac_type = '商业银行'
    elif file_name == '61家拥有银行卡收单资质机构的机构代码.txt':
        ac_type = '其他收单机构'
    elif file_name == '全国119家村镇银行收单机构号大全.txt':
        ac_type = '村镇银行'
    elif file_name == '全国70家农商银行收单机构号大全.txt':
        ac_type = '农商银行'
    else:
        ac_type = ''
    return ac_type
