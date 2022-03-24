#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/15 1:37
# @Author   :DKJ
# @File     :06.xpath4K图片解析.py
# @Software :PyCharm

import requests
from lxml import etree
import os
import time
first_url = 'http://pic.netbian.com/4k%s/index.html'
url = 'http://pic.netbian.com/4k%s/index_%s.html'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }

def Download_img(img_url,filename):
    img_page_text = requests.get(img_url, headers=headers).text
    img_tree = etree.HTML(img_page_text)
    detail_img_url = 'http://pic.netbian.com/' + img_tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
    img_name = img_tree.xpath('//div[@class="photo-pic"]/a/img/@alt')[0]
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    try:
        img = requests.get(detail_img_url, headers=headers).content
        with open(filename + '/' + img_name + '.jpg', 'wb') as fp:
            fp.write(img)
        print(detail_img_url, img_name, "下载完成!")
    except Exception as e:
        print(e, "下载出现异常")

def Make_dir(filename):
    if not os.path.exists(filename):
        os.makedirs(filename)
        print('文件重新创建')
    else:
        print('文件已创建')

def Download_page(page_start,page_end):
    if page_start > page_end:
        page_start,page_end = page_end,page_start
    for page in range(page_start, page_end + 1):
        img_url_list = []
        print('正在下载第%d页图片' % page)
        if page == 1:
            new_url = first_url % name
        else:
            new_url = format(url % (name, page))
        response = requests.get(new_url, headers=headers)
        # 获取页面原始编码格式
        # print(response.encoding)
        page_text = response.text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')

        for li in li_list:
            img_url = 'http://pic.netbian.com/' + li.xpath('./a/@href')[0]
            img_url_list.append(img_url)

        for img_url in img_url_list:
            Download_img(img_url, filename)
    print("--------------------------------over!!!--------------------------------")

if __name__ == '__main__':
    select_list = {'美女':'meinv','风景':'fengjing','游戏':'youxi','动漫':'dongman','影视':'yingshi','明星':'mingxing',
            '汽车':'qiche','动物':'dongwu','人物':'renwu','美食':'meishi','综艺':'zongjiao','背景':'beijing'}
    list = ['美女','风景','游戏','动漫','影视','明星','汽车','动物','人物','美食','综艺','背景']
    i = 1
    for l in select_list.keys():
        print(i,l)
        i+=1
    print()
    index = int(input('你想爬取上述哪类型的图片:(输入序号)'))
    name = select_list[list[index-1]]
    print('爬取4K' + list[index-1] + '图片')
    filename = list[index-1]
    Make_dir(filename)
    page_start = int(input('enter start page:'))
    page_end = int(input('enter end page:'))
    Download_page(page_start,page_end)
    time.sleep(30)