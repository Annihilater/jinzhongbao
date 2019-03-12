#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/26 12:04
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : write_to_excel.py
# python 写入 excel 的方法，写入的 data 是双层列表

import xlwt

data = []


# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(sheetname="sheet_name", cell_overwrite_ok=True)

    for x in range(0, len(data)):
        for y in range(0, len(data[x])):
            sheet1.write(x, y, data[x][y], set_style("Times New Roman", 220, True))

    f.save("excel_file_name.xls")


write_excel()
