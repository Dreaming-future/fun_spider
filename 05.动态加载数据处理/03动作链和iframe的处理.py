#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/18 20:30
# @Author   :DKJ
# @File     :03动作链和iframe的处理.py
# @Software :PyCharm

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
actions.click_and_hold(source)
time.sleep(3)
for i in range(5):
    actions.move_by_offset(xoffset=17,yoffset=0).perform()
    time.sleep(0.5)
actions.release()
browser.quit()