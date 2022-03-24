#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/16 16:33
# @Author   :DKJ
# @File     :线程池.py
# @Software :PyCharm
'''
#同步执行
import time
def sayhello(str):
    print("Hello ",str)
    time.sleep(2)
name_list =['xiaozi','aa','bb','cc']
start_time = time.time()
for i in range(len(name_list)):
    sayhello(name_list[i])
print('%d second'% (time.time()-start_time))
'''
#异步基于线程池
import time
from multiprocessing.dummy import Pool
def sayhello(str):
    print("Hello ",str)
    time.sleep(2)
start = time.time()
name_list =['xiaozi','aa','bb','cc']
#实例化线程池对象，开启了4个线程
pool = Pool(4)
pool.map(sayhello,name_list)
pool.close()
pool.join()
end = time.time()
print(end-start)