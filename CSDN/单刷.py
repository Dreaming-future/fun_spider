#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2021/5/11 11:54
# @Author   :DKJ
# @File     :单刷.py
# @Software :PyCharm

import re
import requests
from requests import RequestException
import time
import random
from lxml import etree
proxy = []
with open('ip_proxy.txt','r') as f:
    page = f.readlines()
    for u in page:
        u = u.replace('\n', '')
        proxy.append(u)

def get_page(url,headers,proxy=None):
    try:
        response = requests.get(url, headers=headers,proxies=proxy)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None

def parse_page(html):
    try:
        read_num = int(re.compile('<span.*?read-count.*?(\d+).*?</span>').search(html).group(1))
        title = str(re.compile('<h1.*?title-article.*?>(.+).*?</h1>').search(html).group(1))
        return read_num,title
    except Exception as e:
        print(e,'解析出错')
        return None,None
    
def get_url_list(url = 'https://blog.csdn.net/weixin_45508265?spm=1001.2101.3001.5343&type=blog',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}):
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//a/@href')
    # print(li_list)
    url_list = []
    for old_url in li_list:
        if '/weixin_45508265/article' in old_url and 'category' not in old_url:
            url_list.append(old_url)
    return url_list
USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Opera/8.0 (Windows NT 5.1; U; en)',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
    ]

referer_list = [
            'http://blog.csdn.net/dala_da/article/details/79401163',
            'http://blog.csdn.net/',
            'https://www.sogou.com/tx?query=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F&hdq=sogou-site-706608cfdbcc1886-0001&ekv=2&ie=utf8&cid=qb7.zhuye&',
            'https://www.baidu.com/s?tn=98074231_1_hao_pg&word=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F'
        ]

def main():
    # read_num_last = 0
    sum = 0
    # start = time.time()
    url_list = [
        'https://blog.csdn.net/weixin_45508265/article/details/114663239',
        'https://blog.csdn.net/weixin_45508265/article/details/116273371',
        'https://blog.csdn.net/weixin_45508265/article/details/113066897',
        'https://blog.csdn.net/weixin_45508265/article/details/113354164',
        'https://blog.csdn.net/weixin_45508265/article/details/116194941',
        'https://blog.csdn.net/weixin_45508265/article/details/112907617',
        'https://blog.csdn.net/weixin_45508265/article/details/113122535',
        'https://blog.csdn.net/weixin_45508265/article/details/113394793',
        'https://blog.csdn.net/weixin_45508265/article/details/116425371',
        'https://blog.csdn.net/weixin_45508265/article/details/115967516',
        'https://blog.csdn.net/weixin_45508265/article/details/112914739',
        'https://blog.csdn.net/weixin_45508265/article/details/113504698',
        'https://blog.csdn.net/weixin_45508265/article/details/113061230',
        'https://blog.csdn.net/weixin_45508265/article/details/114702848',
        'https://blog.csdn.net/weixin_45508265/article/details/115982902',
        'https://blog.csdn.net/weixin_45508265/article/details/112918290'
    ]
    url_list = get_url_list()
    # url_list.append('https://blog.csdn.net/KIK9973/article/details/117113424')
    # url_list = ['https://blog.csdn.net/weixin_45508265/article/details/116795919']
    while 1:
        start = time.time()
        headers1 = {
            'Referer': random.choice(referer_list),  # 伪装成从CSDN博客搜索到的文章
            'User-Agent': random.choice(USER_AGENTS),            # 伪装成浏览器
            'sec-ch-ua': 'Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            "Host": "blog.csdn.net",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        }
        

        proxy1 = {
            'http':random.choice(proxy)
        }
        for url in url_list:
            response = get_page(url,headers1,proxy1)
            read_num,title = parse_page(response)
            print(title,'当前阅读量',read_num,url)
            if read_num > 1000:
                url_list.remove(url)
                print(url + '的阅读量超过1000，已删除')
        end = time.time()
        sum += 1
        print('-'*30)
        print('\n')
        use_time = end - start
        print(len(url_list),'篇文章用了 ',use_time,' s')
        print('现在已经刷了 ',sum,' 次了')
        print('\n')
        print('-' * 30)
        if use_time > 60:
            continue
        else:
            time.sleep(40)

        # if read_num_last < int(read_num):
        #     end = time.time()
        #     print('所用时间',end - start)
        #     time.sleep(5)
        #     start = time.time()
        # read_num_last = int(read_num)
        # print(read_num_last)
        # time.sleep(random.randint(5,10)+60)

if __name__ == '__main__':
    main()
