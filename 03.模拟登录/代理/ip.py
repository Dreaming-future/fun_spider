#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   ip.py
# @Time    :   2021/09/30 19:32:52
# @Author  :   DKJ
# @Contact :   1016617094@qq.com
# @Software:   VScode

# here put the import lib
import requests
from lxml import etree
import random
import os
from pathos.multiprocessing import ProcessingPool as Pool
import time    


my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
PROXY = []
proxies = {}
def read_proxy(path='ip_proxy.txt'):
    if not os.path.exists(path):
        f = open(path,'w')
        f.close()
    with open(path,'r') as f:
        PROXY = f.readlines()
        PROXY = [proxy.replace('\n', '') for proxy in PROXY]
    return PROXY

# 将代理ip写入文件
def write_proxy(proxy,path='ip_proxy.txt'):
    if proxy not in PROXY:
        with open('ip_proxy.txt','a+') as fp:
            fp.write(proxy + '\n')
            print("正在写入 ip: {1} ".format(proxy))
        print("录入完成")
    else:
        print("文件中已有相同ip，未录入")
    
# 验证已得到IP的可用性
def test_proxies(proxies):
    url = "https://www.1688.com/"
    header = {
        "User-Agent": random.choice(my_headers),
        'Connection': 'close'
    }
    for proxy in proxies:
        try:
            response = requests.get(url,headers=header,proxies={"http":proxy,'https':proxy},timeout=2)
            # time = response.elapsed.total_seconds()
            # print(time)
            if response.status_code == 200:
                print('-'*15,"该代理IP可用: {0}".format(proxy),'-'*15)
                write_proxy(proxy)
            else:
                print("该代理IP不可用: {0}".format(proxy))
        except Exception as e:
            print("该代理IP无效: {0}".format(proxy))
    

# 解析网页，并得到网页中的代理IP
def get_proxy(html,xpath):
    selector = etree.HTML(html)
    proxies = []
    XPATH = xpath
    for each in selector.xpath(XPATH):
        # ip.append(each[0])
        ip = each.xpath('./td[1]/text()')[0].strip()
        port = each.xpath('./td[2]/text()')[0].strip()
        proxy = ip + ':' + port
        proxies.append(proxy)
    # print('ip 有' ,len(proxies) , '条')
    test_proxies(proxies)
    
# 营造请求头，获取网页响应
def get_html(url_xpath,page):
    header = {
        "User-Agent": random.choice(my_headers),
        'Connection': 'close',
        'Accept-Language':'zh-CN,zh;q=0.9'
    }
    url,xpath = url_xpath['url'],url_xpath['xpath']
    # print(url,xpath)
    response = requests.get(url%page, headers=header,proxies=proxies)
    # print(response.text)
    get_proxy(response.text ,xpath)
 
 
def test_files(path):
    proxies = read_proxy(path)
    proxies = list(set(proxies))
    url = "https://www.1688.com/"
    header = {
        "User-Agent": random.choice(my_headers),
        'Connection': 'close',
        'Accept-Language':'zh-CN,zh;q=0.9'
    }
    f = open(path,'w')
    for proxy in proxies:
        try:
            response = requests.get(url,headers=header,proxies={"http":proxy,'https':proxy},timeout=3)
            # time = response.elapsed.total_seconds()
            # print(time)
            if response.status_code == 200:
                print('-'*15,"该代理IP可用: {0}".format(proxy),'-'*15)
                f.write(proxy + '\n')
            else:
                print("该代理IP不可用: {0}".format(proxy))
        except Exception as e:
            print("该代理IP无效: {0}".format(proxy))
    f.close()    
    
if __name__ == "__main__":
    requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    # 代理ip的爬取源地址
    PATH = 'ip_proxy.txt'
    test_files(PATH)
    print('测试完毕')
    # time.sleep(10)
    PROXY = read_proxy(PATH)
    if len(PROXY) !=  0:
        proxy = random.choices(PROXY)
        proxies['https'],proxies['http'] = proxy,proxy
    ip_url = {
        # '飞度代理':{'url':'http://www.feidudaili.com/index/gratis/index?page=%s',
        #               'xpath':'//div[@class="section clearfix"]//table[@class="data_table"]/tbody/tr',
        #               'page':24},
        # '齐云代理':{'url':'https://proxy.ip3366.net/free/?action=china&page=%s',
        #               'xpath':'//*[@id="content"]/section/div[2]/table/tbody/tr',
        #               'page':10},
        # '66免费代理':{'url':'http://www.66ip.cn/%s.html',
        #           'xpath':'//div[@class="layui-row layui-col-space15"]//table/tbody/tr',
        #           'page':1000},
        # '云代理':{'url':'http://www.ip3366.net/?stype=1&page=%s',
        #              'xpath':'//div[@id="container"]//div[@id="list"]/table/tbody/tr',
        #              'page':10},
        # '89代理':{'url':'http://www.89ip.cn/index_%s.html',
        #               'xpath':'//table[@class="layui-table"]/tbody/tr',
        #               'page':110},
        'UU http代理':{'url':'http://www.uuhttp.com/index/free/index?page=%s&is_cn=0&gn=0',
                     'xpath':'//div[@class="dial_left fadeInLeft free_page"]//div[@class="price_table"]//tbody/tr',
                     'page': 100},
              }
    # get_html(ip_url['89代理'],1)
    s_pages = 1
    pool = Pool(30)
    for name,ip in ip_url.items():
        # print(name,ip)    
        e_pages = ip['page']
        total_page = [i for i in range(s_pages,e_pages + 1)]    
        url_xpath = [ip]*(e_pages-s_pages + 1)
        pool.map(get_html,url_xpath,total_page)
        print('\n'*3,name,'已经被爬完','\n'*3)
        time.sleep(30)
    pool.close()
    pool.join()