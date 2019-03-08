#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/3 02:03
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test1.py

data_list = []
for i in range(1, 10001):
    # 添加所有任务到总的任务列表
    result = (i, 'zhangsan' + str(i), 'male', 'zhangsan' + str(i) + '@qq.com')
    data_list.append(result)
print(data_list)
