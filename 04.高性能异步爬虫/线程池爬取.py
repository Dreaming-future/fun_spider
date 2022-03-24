#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/16 17:05
# @Author   :DKJ
# @File     :线程池爬取.py
# @Software :PyCharm

import requests
import random
from lxml import etree
import re
# from fake_useragent import UserAgent
#安装fake-useragent库:pip install fake-useragent
#导入线程池模块
from multiprocessing.dummy import Pool
#实例化线程池对象
pool = Pool()
url = 'http://www.pearvideo.com/category_1'
#随机产生UA
# ua = UserAgent().random
headers = {
    #定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
 }
#获取首页页面数据
page_text = requests.get(url=url,headers=headers).text
#对获取的首页页面数据中的相关视频详情链接进行解析
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@id="listvideoList"]/ul/li')
detail_urls = []#存储二级页面的url
for li in li_list:
    detail_url = 'http://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    title = li.xpath('.//div[@class="vervideo-title"]/text()')[0]
    detail_urls.append(detail_url)
vedio_urls = []#存储视频的url
for url in detail_urls:
    page_text = requests.get(url=url,headers=headers).text
    vedio_url = re.findall('srcUrl="(.*?)"',page_text,re.S)[0]
    vedio_urls.append(vedio_url)
#使用线程池进行视频数据下载
func_request = lambda link:requests.get(url=link,headers=headers).content
video_data_list = pool.map(func_request,vedio_urls)

def save(data):
    fileName = str(random.randint(1, 10000)) + '.mp4'
    with open(fileName, 'wb') as fp:
        fp.write(data)
        print(fileName + '已存储')
#使用线程池进行视频数据保存
func_saveData = lambda data:save(data)
pool.map(func_saveData,video_data_list)

pool.close()
pool.join()