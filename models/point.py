#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/4 14:28
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : point.py
from sqlalchemy import Integer, Column, DateTime, String

from models.base import Base


class Point(Base):
    __tablename__ = 'point'
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime())
    update_time = Column(DateTime())
    merc_num = Column(String(30))
    merc_name = Column(String(50))
    mcc = Column(Integer)
    mcc_type = Column(String(30))
    trade_type = Column(String(30))
    cmb_jf = Column(Integer)

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
