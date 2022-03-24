#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/18 17:22
# @Author   :DKJ
# @File     :02selenium自动化操作.py
# @Software :PyCharm


from selenium import webdriver
from time import sleep



bro = webdriver.Chrome(r'D:/PycharmProjects/爬虫/05.动态加载数据处理/chromedriver.exe')
bro.get('https://baidu.com')

bro.get('https://taobao.com')
bro.back()
bro.forward()
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
search_input = bro.find_element_by_id('q')
search_input.send_keys('Iphone')
sleep(2)
search_input.clear()
search_input.send_keys('书包')
button = bro.find_element_by_class_name('btn-search')
button.click()
sleep(2)
bro.quit()

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.jd.com/')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("123")')