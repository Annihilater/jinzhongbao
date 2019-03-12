#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/5 16:14
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : area.py
from sqlalchemy import Column, Integer, DateTime, String

from models.base import Base


class Area(Base):
    __tablename__ = "area"
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime())
    update_time = Column(DateTime())
    area_code = Column(String(50))
    area_name = Column(String(200))
    province_name = Column(String(100))
    province_code = Column(String(50))

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
