#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/14 18:18
# @Author   :DKJ
# @File     :01.正则解析.py
# @Software :PyCharm

import requests
import re
import os
if __name__ == '__main__':
    first_url = 'http://pic.netbian.com/4kmeinv/index.html'
    url = 'http://pic.netbian.com/4kmeinv/index_%s.html'
    headers ={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    # 指定起始也结束页码
    page_start = int(input('enter start page:'))
    page_end = int(input('enter end page:'))
    # 创建文件夹
    if not os.path.exists('images'):
        os.mkdir('images')

    for page in range(page_start,page_end+1):
        print('正在下载第%d页图片'%page)
        if page == 1:
            new_url = first_url
        else:
            new_url= format(url%page)
        page_text = requests.get(new_url, headers=headers).text
        ex = '<img src="(.*?).jpg" alt=".*?">'
        image_url_list = re.findall(ex,page_text,re.S)

        for image_url in image_url_list:
            image_url = 'http://pic.netbian.com' + image_url + '.jpg'
            # print(image_url)
            image_name = image_url.split('/')[-1]
            image_path = 'images/' + image_name
            image = requests.get(image_url,headers=headers).content
            with open(image_path,'wb') as fp:
                fp.write(image)
            print(image_name,'下载成功！')
    print("over")
