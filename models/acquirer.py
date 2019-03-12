#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/5 16:09
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : acquirer.py
from sqlalchemy import Column, Integer, String, DateTime

from models.base import Base


class Acquirer(Base):
    __tablename__ = "acquirer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime())
    update_time = Column(DateTime())
    ac_type = Column(String(200))
    ac_code = Column(String(20))
    area_code = Column(String(20))
    ac_name = Column(String(200))

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
