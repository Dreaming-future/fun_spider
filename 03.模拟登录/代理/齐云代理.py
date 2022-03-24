#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/16 14:42
# @Author   :DKJ
# @File     :齐云代理.py
# @Software :PyCharm

import requests
from lxml import etree


# 将能用的代理IP追加到文件
def write_proxy(proxies):
    print(proxies)
    for proxy in proxies:
        with open('./齐云ip_proxy.txt','a+') as fp:
            print("正在写入:",proxy)
            fp.write(proxy + '\n')
    print("录入完成")


# 解析网页，并得到网页中的代理IP
def get_proxy(html):
    selector = etree.HTML(html)
    proxies = []
    for each in selector.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr'):
    # for each in selector.xpath('//table[@class="layui-table"]/tbody/tr')[1:]:
        # ip.append(each[0])
        ip = each.xpath('./td[1]/text()')[0].strip()
        port = each.xpath('./td[2]/text()')[0].strip()
        proxy = ip + ':' + port
        proxies.append(proxy)
    print(proxies)
    test_proxies(proxies)

# 验证已得到IP的可用性
def test_proxies(proxies):
    proxies = proxies
    url = "https://www.1688.com/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    normal_proxies = []
    count = 1
    for proxy in proxies:
        print("第%s个。。"%count)
        count += 1
        try:
            response = requests.get(url,headers=header,proxies={"https":proxy},timeout=1)
            time = response.elapsed.total_seconds()
            print(time)
            if response.status_code == 200:
                print("该代理IP可用:",proxy)
                normal_proxies.append(proxy)
            else:
                print("该代理IP不可用:",proxy)
        except Exception as e:
            print(str(e),"该代理IP无效:",proxy)
            pass
    write_proxy(normal_proxies)

# 营造请求头，获取网页响应
def get_html(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    response = requests.get(url, headers=header, )
    # print(response.text)
    get_proxy(response.text)


if __name__ == "__main__":
    # base_url = "https://www.kuaidaili.com/free/inha/%s/"
    # base_url = 'http://www.89ip.cn/index_%s.html'
    base_url = 'https://proxy.ip3366.net/free/?action=china&page=%s'
    for i in range(1, 10):
        url = base_url % i
        get_html(url)