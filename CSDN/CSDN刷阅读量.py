#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2021/5/10 22:24
# @Author   :DKJ
# @File     :刷阅读量.py
# @Software :PyCharm

import re
import requests
from requests import RequestException
import time
import random
from lxml import etree
# url = []
# with open('url.txt','r') as f:
#     page = f.readlines()
#     for u in page:
#         u = u.replace('\n','')
#         url.append(u)
# # print(url)
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36',
    'referer':'https://blog.csdn.net/weixin_45508265?spm=1001.2227.3001.5343&type=lately',
    'sec-ch-ua':'Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    }

def get_page(url):
    try:
        headers = {
            'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
            # 伪装成浏览器
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None

def parse_page(html):
    try:
        read_num = int(re.compile('<span.*?read-count.*?(\d+).*?</span>').search(html).group(1))
        return read_num
    except Exception:
        print('解析出错')

def get_url_list(url = 'https://blog.csdn.net/weixin_45508265?spm=1001.2101.3001.5343&type=blog'):
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//a/@href')
    # print(li_list)
    url_list = []
    for old_url in li_list:
        if '/weixin_45508265/article/details/' in old_url:
            url_list.append(old_url)
    return url_list

proxy = []
with open('ip_proxy.txt','r') as f:
    page = f.readlines()
    for u in page:
        u = u.replace('\n', '')
        proxy.append(u)

proxies = {}
url = get_url_list('https://blog.csdn.net/weixin_45508265?spm=1001.2101.3001.5343&type=blog')
print(url)
# url = ['https://blog.csdn.net/weixin_45508265/article/details/114663239']

for i in range(10000):
    proxies['http'] = proxy[random.randint(0,len(proxy)-1)]
    u = url[random.randint(0,len(url)-1)]
    print('第%d次刷新\n' % i,'网址为:',u,'proxy',proxies['http'])
    time.sleep(2)
    req = requests.get(url = u,headers=headers,proxies=proxies)
    print('当前阅读量：',parse_page(u))
    print('第%d次结束\n' % i)
# import re
# import requests
# from requests import RequestException
# import time
# import random
# from lxml import etree
#
# headers = {
#             'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
#             # 伪装成浏览器
#         }
# def get_page(url):
#     try:
#         headers = {
#             'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
#             # 伪装成浏览器
#         }
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         print('请求出错')
#         return None
#
# def parse_page(html):
#     try:
#         read_num = int(re.compile('<span.*?read-count.*?(\d+).*?</span>').search(html).group(1))
#         return read_num
#     except Exception:
#         print('解析出错')
#         return None
#
# def get_url_list(url = 'https://blog.csdn.net/weixin_45508265?spm=1001.2101.3001.5343&type=blog'):
#     page_text = requests.get(url=url,headers=headers).text
#     tree = etree.HTML(page_text)
#     li_list = tree.xpath('.//div[@class="navList-box"]//a/@href')
#     # print(li_list)
#     url_list = []
#     for old_url in li_list:
#         if 'download' not in old_url:
#             url_list.append(old_url)
#     return url_list
#
# def save_file(path,lists):
#     with open(path,'w') as f:
#         for list in lists:
#             f.write(list+'\n')
#
# def get_proxy_list(path):
#     proxy = []
#     with open(path, 'r') as f:
#         page = f.readlines()
#         for u in page:
#             u = u.replace('\n', '')
#             proxy.append(u)
#     return proxy
#
# def main():
#     # url = input('请输入正确的CSDN博客地址:')
#     # url_list = get_url_list(url)
#     proxy_list = get_proxy_list('89ip_proxy.txt')
#     times = 0
#     finished_times = 0
#     while 1:
#         user_agent_list = [
#             {'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'},
#             {'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)'},
#             {'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'},
#             {'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'},
#             {'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'},
#             {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'},
#             {'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'},
#             {'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'},
#             {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'},
#             {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'}
#         ]
#
#         referer_list = [
#             {'http://blog.csdn.net/dala_da/article/details/79401163'},
#             {'http://blog.csdn.net/'},
#             {'https://www.sogou.com/tx?query=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F&hdq=sogou-site-706608cfdbcc1886-0001&ekv=2&ie=utf8&cid=qb7.zhuye&'},
#             {'https://www.baidu.com/s?tn=98074231_1_hao_pg&word=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F'}
#         ]
#         # 想要刷的blog的url
#         url = 'https://blog.csdn.net/zhang__shuang_/article/details/82527314'
#         # 随机user_agent和Referer
#         header = {'User-Agent': random.choice(user_agent_list),
#                   'Referer': random.choice(referer_list)
#         }
#         # 依次从proxy_list中取
#         ip = proxy_list[times % len(proxy_list)]
#         # 设置代理,格式如下
#         # proxy_ip = 'http://' + ip
#         # proxy_ips = 'https://' + ip
#         proxy_ip = ip
#         proxy_ips = ip
#         proxy = {'https': proxy_ips, 'http': proxy_ip}
#         try:
#             response = requests.get(url, headers=header, proxies=proxy)
#         except:
#             # 无响应则print出该代理ip
#             print('代理出问题啦:',proxy["https"])
#             time.sleep(0.1)
#         else:
#             print('已刷%d次,%s') % (finished_times + 1, proxy["https"])
#             time.sleep(random.random())
#             finished_times += 1
#
#         times += 1
#         # 每当所有的代理ip刷过一轮，延时15秒
#         if not times % len(proxy_list):
#             time.sleep(15)
#
# if __name__ == '__main__':
#     main()