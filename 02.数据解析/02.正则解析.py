#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/14 20:23
# @Author   :DKJ
# @File     :02.正则解析.py
# @Software :PyCharm

import os
import requests
import re

if __name__ == '__main__':
    list = ['meinv','fengjing','youxi','dongman','yingshi','mingxing','qiche','dongwu','renwu','meishi','zongjiao','beijing']
    first_url = 'http://pic.netbian.com/4k%s/index.html'
    url = 'http://pic.netbian.com/4k%s/index_%s.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    for name in list:
        print('爬取4K' + name + '图片')
        filename = name
        if not os.path.exists(filename):
            os.makedirs(filename)
        page_start = int(input('enter start page:'))
        page_end = int(input('enter end page:'))
        if page_start > page_end:
            page_start,page_end = page_end,page_start
        for page in range(page_start, page_end + 1):
            image_url_list = []
            print('正在下载第%d页图片' % page)
            if page == 1:
                new_url = first_url%name
            else:
                new_url = format(url % (name,page))
            response = requests.get(new_url,headers = headers)
            ex = '<a href="/tupian/(.*?)" target="_blank">'
            page_text = response.text
            url_list = re.findall(ex,page_text,re.S)
            # print(url_list)
            for url2 in url_list:
                new_url = 'http://pic.netbian.com/tupian/'+url2
                ex2 = '<img src="(.*?)" data-pic=".*?"'
                image_url_list.append(re.findall(ex2,requests.get(new_url,headers=headers).text,re.S)[0])
            # print(image_url_list)
            for image_url in image_url_list:
                image_url = 'http://pic.netbian.com/' + image_url
                image_name = image_url.split('/')[-1]
                image_path = filename + '/' + image_name
                image = requests.get(image_url, headers=headers).content
                with open(image_path, 'wb') as fp:
                    fp.write(image)
                print(image_name, '下载成功！')
    print("over")