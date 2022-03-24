#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/12 19:22
# @Author   :DKJ
# @File     :crawler.py
# @Software :PyCharm

from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://movie.douban.com/subject/1292052/')
title = r.html.find('#content > h1 > span:nth-child(1)', first=True)
# r.html.find() 接受一个 CSS 选择器（字符串形式）作为参数
# 返回在网页中使用该选择器选中的内容。

print(title.text)