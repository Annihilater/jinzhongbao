#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/1 16:53
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : trade.py
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.mysql import FLOAT

from models.base import Base


class Trade(Base):
    __tablename__ = "trade"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    create_time = Column(DateTime())
    update_time = Column(DateTime())
    year = Column(String(10))
    month = Column(String(10))
    day = Column(String(10))
    TRTM = Column("time", String(20))
    RN = Column("rn", Integer())
    MERCHANT_ORDER_NAME = Column("merchant_order_name", String(100))
    merc_num = Column(String(20))
    TRADE_AMOUNT = Column("trade_amount", Integer())
    AMOUNT = Column("amount", FLOAT(precision=10, scale=2), default=0.00)
    RECEIPT_AMOUNT_FEE = Column(
        "receipt_amount_fee", FLOAT(precision=10, scale=2), default=0.00
    )
    JSSTATUS = Column("js_status", String(20))
    bank = Column(String(20))
    CARDNO = Column("card_no", String(30))

    JYSTATUS = Column("jy_status", String(10))
    SEQNO = Column("seqno", String(50))
    MERCHANT_ORDER_NAME_OLD = Column("merchant_order_name_old", String(30))
    THUUID = Column("thuuid", String(100))
    trade_detail_url = Column(String(1000))
    receipt_url = Column(String(300))

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
