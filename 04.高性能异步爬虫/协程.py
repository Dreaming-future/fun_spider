#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/18 0:50
# @Author   :DKJ
# @File     :协程.py
# @Software :PyCharm

# 异步协程用法
# 从 Python 3.4 开始，Python 中加入了协程的概念，但这个版本的协程还是以生成器对象为基础的，在 Python 3.5 则增加了 async/await，使得协程的实现更加方便。
# 首先我们需要了解下面几个概念：

# event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。程序是按照设定的顺序从头执行到尾，
# 运行的次数也是完全按照设定。当在编写异步程序时，必然其中有部分程序的运行耗时是比较久的，需要先让出当前程序的控制权，让其在背后运行，让另一部分的程序先运行起来。
# 当背后运行的程序完成后，也需要及时通知主程序已经完成任务可以进行下一步操作，但这个过程所需的时间是不确定的，需要主程序不断的监听状态，一旦收到了任务完成的消息，
# 就开始进行下一步。loop就是这个持续不断的监视器。

# coroutine：中文翻译叫协程，在 Python 中常指代为协程对象类型，我们可以将协程对象注册到事件循环中，它会被事件循环调用。我们可以使用 async 关键字来定义一个方法，
# 这个方法在调用时不会立即被执行，而是返回一个协程对象。

# task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。

# future：代表将来执行或还没有执行的任务，实际上和 task 没有本质区别。

# 另外我们还需要了解 async/await 关键字，它是从 Python 3.5 才出现的，专门用于定义协程。其中，async 定义一个协程，await 用来挂起阻塞方法的执行。

# 定义一个协程
# import asyncio
# async def execute(x):
#     print('Number:', x)
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('After calling loop')

# task的使用
# import asyncio
# async def execute(x):
#     print('Number:', x)
#     return x
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('Task:', task)
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')

# ensure_future()的使用
# import asyncio
# async def execute(x):
#     print('Number:', x)
#     return x
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
# task = asyncio.ensure_future(coroutine)
# print('Task:', task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')

# 绑定回调
import asyncio
import requests
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url).status_code
    return status
def callback(task):
    print('Status:', task.result())
coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)