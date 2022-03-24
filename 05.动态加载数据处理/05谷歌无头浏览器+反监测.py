#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/18 20:54
# @Author   :DKJ
# @File     :05谷歌无头浏览器+反监测.py
# @Software :PyCharm

import time
from selenium import webdriver
# 实现无可视化页面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 驱动路径
path = r'./chromedriver'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options,options=option)
# 上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)
browser.save_screenshot('baidu.png')
browser.quit()