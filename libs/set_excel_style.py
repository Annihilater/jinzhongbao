#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/3 11:34
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : set_excel_style.py
import xlwt


def set_style(name, height, bold=False):  # 设置表格样式
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style
