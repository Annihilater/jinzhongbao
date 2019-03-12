#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/2 03:30
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : generate_begin_date.py
from sqlalchemy import func

from config import BEGIN_DATE
from data_base.database import db
from models.trade import Trade


def generate_begin_date():
    """
    设定本次抓去的开始月
    从数据库查出最后一次抓取数据的月份，设为本次抓取的开始月；
    如果没有数据，则将最开始交易的日期设为抓取的开始月。
    """
    max_id = db.session.query(func.max(Trade.id)).scalar()
    if max_id:
        y, m, d = db.session.query(
            Trade.year, Trade.month, Trade.day).filter_by(
            id=max_id).first()
        begin_date = y + m
    else:
        begin_date = BEGIN_DATE
    return begin_date
