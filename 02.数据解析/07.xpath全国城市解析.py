#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/15 9:36
# @Author   :DKJ
# @File     :07.xpath全国城市解析.py
# @Software :PyCharm


import requests
from lxml import etree
url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
#获取页面原始编码格式
print(response.encoding)
page_text = response.text
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul//li')
for li in li_list:
    city_name = li.xpath('./a/text()')[0]
    city_url = 'https://www.aqistudy.cn/historydata/'+li.xpath('./a/@href')[0]
    print(city_name,city_url)