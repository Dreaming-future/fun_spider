#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/3/13 10:37
# @Author   :DKJ
# @File     :example1.py
# @Software :PyCharm

import requests
from selenium import webdriver
import time
import random

option=webdriver.ChromeOptions()
# option.add_argument('--headless')
# option.add_argument('--no-sandbox')
# option.add_argument('--start-maximized')

url=["https://blog.csdn.net/weixin_45508265/article/details/116568820",
    "https://blog.csdn.net/weixin_45508265/article/details/116358751",
     "https://blog.csdn.net/weixin_45508265/article/details/116311272",
     "https://blog.csdn.net/weixin_45508265/article/details/116308862",
     "https://blog.csdn.net/weixin_45508265/article/details/116273921",
     "https://blog.csdn.net/weixin_45508265/article/details/115982902",
     "https://blog.csdn.net/weixin_45508265/article/details/113775898",
     "https://blog.csdn.net/weixin_45508265/article/details/114702848",
     "https://blog.csdn.net/weixin_45508265/article/details/114664548",
     "https://blog.csdn.net/weixin_45508265/article/details/114642141",
     ]

for i in range(1000):
    print('第%d次刷新\n'%i)
    try:
        driver = webdriver.Chrome(r'D:/PycharmProjects/爬虫/05.动态加载数据处理/chromedriver.exe', options=option)
        driver.get(url[i%10])
        driver.refresh()
        print('test pass: refresh successfull')
        # driver.get_screenshot_as_file('%d.png'%i)
        time.sleep(2)
        print('第%d次结束\n' % i)
        driver.quit()
    except Exception as e:
        print('Exception found',e)
        driver.quit()
    if i%10 == 9:
        time.sleep(60+random.randint(1,10))
        print('休眠60s')
