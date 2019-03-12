#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/2 21:11
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : black_list.py
from sqlalchemy import Column, String, Integer, DateTime

from models.base import Base


class BlackList(Base):
    __tablename__ = "cmb_black_list"
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime())
    update_time = Column(DateTime())
    cmb_update_time = Column(DateTime())
    merc_num = Column(String(50))
    merc_name = Column(String(200))
    acquirer_num = Column(String(3))
    acquirer_name = Column(String(100))
    mcc = Column(String(4))
    mcc_type = Column(String(30))
    area_num = Column(String(4))
    area_name = Column(String(100))
    merc_seq_num = Column(String(30))
    trade_type = Column(String(30))
    cmb_jf = Column(Integer)

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
