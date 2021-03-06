#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/21 11:55
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test_img_ocr.py

from PIL import Image
import pytesseract

from config import IMAGE_PATH

image = Image.open(IMAGE_PATH)
code = pytesseract.image_to_string(image, lang="chi_sim", config="psm 6")
print(code)
