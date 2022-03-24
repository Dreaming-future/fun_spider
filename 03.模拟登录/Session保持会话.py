#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/23 16:04
# @Author   :DKJ
# @File     :Session保持会话.py
# @Software :PyCharm

import requests

s = requests.Session()
r = s.get('http://httpbin.org/cookies/set/number/123456789')
print(r.cookies)
r = s.get('http://httpbin.org/cookies')
print(r.text)