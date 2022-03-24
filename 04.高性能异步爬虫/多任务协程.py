#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/18 10:36
# @Author   :DKJ
# @File     :多任务协程.py
# @Software :PyCharm


# 多任务协程
# 如果我们想执行多次请求应该怎么办呢？我们可以定义一个 task 列表，然后使用 asyncio 的 wait() 方法即可执行。
# import asyncio
# import time
# async def request(url):
#     print('正在下载',url)
#     #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
#     time.sleep(2)
#     print('下载完毕',url)
# start = time.time()
# urls = [
#     'www.baidu.com',
#     'www.sogou.com',
#     'www.goubanjia.com'
# ]
# #任务列表：存放多个任务对象
# stasks = []
# for url in urls:
#     c = request(url)
#     task = asyncio.ensure_future(c)
#     stasks.append(task)
# loop = asyncio.get_event_loop()
# #需要将任务列表封装到wait中
# loop.run_until_complete(asyncio.wait(stasks))
# print(time.time()-start)

# 注意：在实现异步环节的编码中不可以出现非异步模块的代码，否则就无法实现真正的异步了。上述案例中的time.sleep就是非异步模块中的代码。因此改写成：
import asyncio
import time
async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    # time.sleep(2)
    #当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完毕',url)
start = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com'
]
#任务列表：存放多个任务对象
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
print(time.time()-start)


