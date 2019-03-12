#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/1 22:55
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : bank.py
import json
import requests

from config import JD_QUICK_PASS_BIN
from data_base.database import db
from models.trade import Trade


def which_bank(c):
    base_url = 'https://ccdcapi.alipay.com/validateAndCacheCardInfo.json?' \
               '_input_charset=utf-8&cardNo=银行卡卡号&cardBinCheck=true'
    url = base_url.replace('银行卡卡号', c)

    response = requests.post(url)
    d = json.loads(response.text)
    if d['validated'] is False and c[:6] == JD_QUICK_PASS_BIN:
        print(c, d['messages'])
        d['bank'] = '京东闪付虚拟卡'
    return d['bank']


def change():
    """
    更新 trade 表的 bank 字段
    :return:
    """
    for i in [358, 364]:
        try:
            trade = db.session.query(Trade).get(ident=i)
        except Exception as e:
            break
        if trade:
            card_no = generate_card(trade.CARDNO)

            try:
                bank = which_bank(card_no)
            except Exception as e:
                continue

            with db.auto_commit():
                db.session.query(Trade).filter_by(
                    id=i).update({Trade.bank: bank})


def generate_card(card):  # 银行卡一般为16位，前6位为发卡行 BIN 号，这里加0是为了补全卡号发给阿里 api 识别发卡行
    c = card[:6] + '0000000000'
    return c


if __name__ == '__main__':
    change()
