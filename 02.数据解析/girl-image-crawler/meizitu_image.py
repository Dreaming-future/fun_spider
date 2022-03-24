#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/17 10:21
# @Author   :DKJ
# @File     :meizitu_image.py
# @Software :PyCharm

import requests
from lxml import etree
import time
import os
from multiprocessing import Pool


def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36",
    }
    proxies = {
        'http':''
    }
    response = requests.get(url=url,headers=headers)
    return response

# 获得每一页的url
def get_pages(page_start,page_end):
    url = 'https://www.mzitu.com/page/%s/'
    start_url = format(url%page_start)
    response = get_response(start_url)
    page_urls = []
    page_urls.append(start_url)
    while True:
        parsed_body = etree.HTML(response.text)
        next_url = parsed_body.xpath('//div[@class="nav-links"]/a[@class="next page-numbers"]/@href')[0]
        if not next_url:
            break
        if next_url == url%(page_end+1):
            break
        page_urls.append(next_url)

        response = get_response(next_url)
    print("get pages done!!!")
    return page_urls

# 在每个页码爬取每个女孩专辑的页面
def get_girl(url):
    response = get_response(url)
    parsed_body = etree.HTML(response.text)
    girl = parsed_body.xpath('//ul[@id="pins"]/li/a/@href')
    return girl

# 美女的名字和所有图片的url
def get_girl_pages(girl_url):
    image_girl_urls = []
    response = get_response(girl_url)
    print(response.status_code)
    paresd_body = etree.HTML(response.text)
    name = paresd_body.xpath('//h2[@class="main-title"]/text()')
    # image_girl_urls.append(girl_url)
    number = girl_url.split('/')[-1]
    while True:
        paresd_body = etree.HTML(response.text)
        next_url = paresd_body.xpath('//div[@class="pagenavi"]/a/@href')[-1]
        image_girl_url = paresd_body.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        print(next_url)
        if not next_url:
            break
        image_girl_urls.append(image_girl_url)
        if next_url.split('/')[-2] != number:
            break
        response = get_response(next_url)
    return name,image_girl_urls

# def get_girls_image(page_start,page_end,girl_urls):
#     pool = Pool(6)
#     image = []
#     for i in range(page_end-page_start):
#         image.append(pool.map(get_girl_pages,girl_urls[i]))
#     return image


def get_girl_image(url):
    name, girl = get_girl_pages(url)
    print(girl)
    print(name[0], len(girl))
    dir_name = './img2/' + name[0]
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    print(name[0], "      正在下载！！！")
    for url in girl:
        count = 1
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36",
            "Referer": url + str(count)
        }
        with open(dir_name + '/' + url.split('/')[-1], 'wb') as fp:
            response = requests.get(url, headers=headers)
            fp.write(response.content)
        count += 1
    print(name[0], "      下载完成！！！")

if __name__ == '__main__':
    # page_start = int(input('开始爬取的页码：'))
    # page_end = int(input('爬取结束的页码：'))
    start_time = time.time()
    # page_urls = get_pages(page_start,page_end)
    # print(page_urls)
    # pool = Pool(6)
    # girl_urls = pool.map(get_girl,page_urls)
    # print(girl_urls)
    # images =pool.map(get_girl_pages,girl_urls[0])
    # # images = get_girls_image(page_start, page_end, girl_urls)
    # print(images)
    # pool = Pool(6)
    # for i in range(page_end-page_start+1):
    #     pool.map(get_girl_image,girl_urls[i])
    # pool.close()
    # pool.join()

    url = 'https://www.mzitu.com/234343'
    # url = 'https://www.mzitu.com/64588'
    name, girl = get_girl_pages(url)
    print(girl)
    print(name[0], len(girl))
    dir_name = './img2/' + name[0]
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    print(name[0], "      正在下载！！！")
    for url in girl:
        count = 1
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36",
            "Referer": url + str(count)
        }
        with open(dir_name + '/' + url.split('/')[-1], 'wb') as fp:
            response = requests.get(url, headers=headers)
            fp.write(response.content)
        count += 1
    print(name[0], "      下载完成！！！")
    # get_girl_image(url)
    end_time = time.time()
    elapsed_time = time.time() - start_time
    print()
    print("elasped %s seconds!!!!" % elapsed_time)