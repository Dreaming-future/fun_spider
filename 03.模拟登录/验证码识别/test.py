#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/19 17:45
# @Author   :DKJ
# @File     :test.py
# @Software :PyCharm

# 图形验证码的识别
# 图形验证码的识别
import tesserocr
from PIL import Image

image = Image.open('./code.png')
result = tesserocr.image_to_text(image)
print(result)

