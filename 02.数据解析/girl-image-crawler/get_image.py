#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/15 15:11
# @Author   :DKJ
# @File     :get_image.py
# @Software :PyCharm

import os
import requests
import time
from lxml import html
def get_response(url):
    headers ={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36",
        'Referer': 'http://static.meinvjpg.com/static/fonts/font-awesome/css/font-awesome.min.css',
    }
    response = requests.get(url,headers=headers)
    return response
# 获得每个页面的url
def get_page_urls():
    start_page = int(input('爬取的开始页码是:'))
    end_page = int(input('爬取的截止页码是:(216为最终页)'))
    head_url = 'http://girl-atlas.net/'
    start_url = format('http://girl-atlas.net/?p=%s'%start_page)
    response = get_response(start_url)
    page_urls = []
    page_urls.append(start_url)
    while True:
        parsed_body = html.fromstring(response.text)
        next_url = parsed_body.xpath('//ul[@class="pagination"]/li/a/@href')
        if not next_url:
            break
        next_url = head_url + next_url[-1]
        if end_page == 216:
            if next_url == 'http://girl-atlas.net/javascript:;':
                break
        else:
            if next_url == format('http://girl-atlas.net/?p=%s'%(end_page+1)):
                break
        # print(next_url)
        page_urls.append(next_url)
        response = get_response(next_url)
    print("get_page_urls done!!!")
    print(page_urls)
    return page_urls

# 获取每个girl专辑的Url
def get_girl_urls(page_urls):
    girl_urls = []

    for url in page_urls:
        # print(url)
        response = get_response(url)
        parsed_body = html.fromstring(response.text)
        girl = parsed_body.xpath('//div[@class="container"]//div[@class="album-item row"]//h2/a/@href')
        # print(girl)
        girl_urls.extend(girl)
    print('get_girl_urls over')
    return girl_urls

def get_image_urls(girl_urls):
    girl_list = []
    for url in girl_urls:
        url = 'http://girl-atlas.net/' + url
        response = get_response(url)
        parsed_body = html.fromstring(response.text)
        # 专辑名
        girl_title = parsed_body.xpath('//div[@class="header-right clearfix"]/h3/text()')
        image_urls = parsed_body.xpath('//li[@class="slide "]/img/@src | //li[@class="slide "]/img/@delay')
        girl_dict = {girl_title[0]: image_urls}

        print(girl_title[0])
        girl_list.append(girl_dict)

    print("get_girl_urls done!!!")
    return girl_list

# 开始下载图片
def get_images(girl_list):
    count = 1

    start_dir = './img/'
    for girl in girl_list:
        print('正在下载第%d组写真集'%count)
        print(list(girl.keys())[0])
        dir_name = start_dir + list(girl.keys())[0]
        urls = list(girl.values())[0]
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
        except Exception as e:
            print(str(e))
            dir_name = start_dir + 'photo album' + str(count)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            print('新目录已创建')
        try:
            for url in urls:
                with open(dir_name.rstrip() + '/' + (url.split('/')[-1]).split('.')[0]+'.jpg','wb') as f:
                    r = get_response(url)
                    f.write(r.content)

            print()
            print(count,list(girl.keys())[0] + "   done!!!")
            print()
        except Exception as e:
            print(str(e))
        count+=1


if __name__ == '__main__':
    page_urls = get_page_urls()
    start_time = time.time()
    girl_urls = get_girl_urls(page_urls)
    girl_list = get_image_urls(girl_urls)
    print("girl %s" % len(girl_urls))
    get_images(girl_list)

    elapsed_time = time.time() - start_time
    print()
    print("elasped %s seconds!!!!" % elapsed_time)
