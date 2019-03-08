#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/1 16:14
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_timestamp.py

import time


def generate_timestamp():
    t = time.time()
    t = int(round(t * 1000))
    return t


if __name__ == '__main__':
    timestamp = generate_timestamp()
    print(timestamp)
