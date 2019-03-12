#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/2 15:09
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test8.py
import json
from urllib.parse import quote
from config import encode_str, dict_record


json_record = json.dumps(dict_record).upper()
print(json_record)
encode_record = quote(json_record.encode("gb2312"))
encode_record = encode_record.replace("%20", "")
print(encode_str)
print(encode_record)
