#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/16 16:30
# @Author   :DKJ
# @File     :单线程.py
# @Software :PyCharm

import requests
def parse_page(res):
    print('解析 %s' %(len(res)))
def get_page(url):
    print('下载 %s' %url)
    response=requests.get(url)
    if response.status_code == 200:
        return response.text
urls = [
    'https://i2.hdslb.com/bfs/face/32f78e427fd6bdbc01dbce3fec5a8180062a321a.jpg@68w_68h.webp',
    'https://i1.hdslb.com/bfs/face/49236950b998d17577e8f47fa1521e9d73950e05.jpg@68w_68h.webp',
    'https://i2.hdslb.com/bfs/face/c4461b83eb9d29bcb9e5d05e98345da2bc58f255.jpg@68w_68h.webp'
]
for url in urls:
    res=get_page(url) #调用一个任务，就在原地等待任务结束拿到结果后才继续往后执行
    parse_page(res)