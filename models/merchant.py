#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/2 17:15
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : merchant.py
from sqlalchemy import Column, Integer, String, DateTime

from models.base import Base


class Merchant(Base):
    __tablename__ = "merchant"
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime())
    update_time = Column(DateTime())
    mcc = Column(Integer)
    mcc_name = Column(String(50))
    mcc_type = Column(String(10))
    IDENAME = Column("merc_name", String(200))
    IDENO = Column("merc_num", String(30))
    province_name = Column(String(100))
    province_id = Column(String(30))
    city_name = Column(String(100))
    city_id = Column(String(30))
    AMT = Column("amt", String(20))
    retmsg = Column("ret_msg", String(100))
    retcode = Column("ret_code", String(100))
    cmb_black_list = Column(Integer)

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
