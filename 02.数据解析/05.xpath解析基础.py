#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/14 23:53
# @Author   :DKJ
# @File     :05.xpath解析基础.py
# @Software :PyCharm

#解析出一级页面的标题和二级页面的价格和描述
import requests
from lxml import etree
import lxml
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url = 'https://bj.58.com/changping/ershoufang/?utm_source=sem-baidu-pc&spm=105916147073.26420796294&PGTID=0d30000c-0000-17fc-4658-9bdfb947934d&ClickID=3'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
# with open('./text.html','w',encoding='utf-8') as f:
#     f.write(page_text)
# tree= etree.parse('./text.html', etree.HTMLParse())
li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
data = []
for li in li_list:
    #解析标题
    title = li.xpath('.//div[@class="list-info"]/h2/a/text()')[0]
    detail_page_url = li.xpath('.//div[@class="list-info"]/h2/a/@href')[0]
    if detail_page_url.split('//')[0] != 'https:':
        detail_page_url = 'https:'+detail_page_url
    detail_text = requests.get(url=detail_page_url,headers=headers).text
    tree = etree.HTML(detail_text)
    #解析二级页面的描述和价格
    desc = ''.join(tree.xpath('//div[@id="generalDesc"]//div[@class="general-item-wrap"]//text()')).strip(' \n \t')
    price = ''.join(tree.xpath('//div[@id="generalExpense"]//div[@class="general-item-wrap"]//text()')).strip(' \n \t')
    dic = {
        'title':title,
        'desc':desc,
        'price':price
    }
    data.append(dic)
    break
#进行持久化存储
print(data)