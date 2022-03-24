#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/3/13 17:06
# @Author   :DKJ
# @File     :example4.py
# @Software :PyCharm


import requests


url="https://m.ip138.com/iplookup.asp?ip="
try:
    r=requests.get(url+'202.200.80.112')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")