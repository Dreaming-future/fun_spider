#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/3/25 16:10
# @Author   :DKJ
# @File     :example_BeautifulSoup.py
# @Software :PyCharm

from bs4 import BeautifulSoup
import requests

url = 'http://python123.io/ws/demo.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    print(soup.prettify())
    tag = soup.a
    #遍历儿子节点
    for child in soup.body.children:
        print(child)
    #遍历子孙节点
    for child in soup.body.descendants:
        print(child)
    #遍历后续节点
    for sibling in soup.a.next_sibling:
        print(sibling)
    #遍历前续节点
    for sibling in soup.a.previous_sibling:
        print(sibling)
except:
    print("error")