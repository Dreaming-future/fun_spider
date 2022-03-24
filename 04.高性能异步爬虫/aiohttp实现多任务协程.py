#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/18 10:49
# @Author   :DKJ
# @File     :aiohttp实现多任务协程.py
# @Software :PyCharm

import requests
import asyncio
import aiohttp
import time

#环境安装：pip install aiohttp
#使用该模块中的ClientSession
import requests
import asyncio
import time
import aiohttp
start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom',
    'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
    'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
    'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
]
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        #get()、post():
        #headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response:
            #text()返回字符串形式的响应数据
            #read()返回的二进制形式的响应数据
            #json()返回的就是json对象
            #注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)
tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('总耗时:',end-start)
# 在这里我们将请求库由 requests 改成了 aiohttp，通过 aiohttp 的 ClientSession 类的 get() 方法进行请求，结果如下：
#
# Hello tom
# Hello jay
# Hello bobo
# Hello bobo
# Hello jay
# Hello bobo
# Hello tom
# Hello jay
# Hello jay
# Hello tom
# Hello tom
# Hello bobo
# 总耗时: 2.037203073501587