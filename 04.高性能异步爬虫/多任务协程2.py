#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/18 10:40
# @Author   :DKJ
# @File     :多任务协程2.py
# @Software :PyCharm

import requests
import asyncio
import time
start = time.time()
urls= {
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
}

async def get_page(url):
    print('正在下载',url)
    response = requests.get(url)
    print('下载完毕',response.text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(end-start)

# 可以发现和正常的请求并没有什么两样，依然还是顺次执行的，耗时 6 秒，平均一个请求耗时 2 秒，说好的异步处理呢？

# 原因在于requests模块是非异步模块，要想实现真正的异步必须使用基于异步的网络请求模块所以这里就需要 aiohttp 派上用场了。