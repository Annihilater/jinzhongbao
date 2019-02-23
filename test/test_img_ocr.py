#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/21 11:55
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_img_ocr.py

from PIL import Image
import pytesseract

from config import image_path

image = Image.open(image_path)
code = pytesseract.image_to_string(image, lang="chi_sim", config="psm 6")
print(code)

