#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/1 21:30
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : base.py
from sqlalchemy.ext.declarative import declarative_base

# 调用 declarative_base 可以产生一个类，这个类和它的子类可以在 base.metadata.create_all()
# 的时候，将接收到的数据自动映射成数据表
Base = declarative_base()
