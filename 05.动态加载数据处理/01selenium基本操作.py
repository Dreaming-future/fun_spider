#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/18 11:08
# @Author   :DKJ
# @File     :01selenium基本操作.py
# @Software :PyCharm

from selenium import webdriver
from time import sleep

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(executable_path='D:/PycharmProjects/05.动态加载数据处理/chromedriver')
# 用get打开百度页面
driver.get("http://www.baidu.com")
# 查找页面的“设置”选项，并进行点击
driver.find_elements_by_link_text('设置')[0].click()
sleep(2)
# # 打开设置后找到“搜索设置”选项，设置为每页显示50条
driver.find_elements_by_link_text('搜索设置')[0].click()
sleep(2)
# 选中每页显示50条
m = driver.find_element_by_id('nr')
sleep(2)
m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
m.find_element_by_xpath('.//option[3]').click()
sleep(2)
# 点击保存设置
driver.find_elements_by_class_name("prefpanelgo")[0].click()
sleep(2)
# 处理弹出的警告页面   确定accept() 和 取消dismiss()
driver.switch_to_alert().accept()
