#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/10 16:41
# @Author   :DKJ
# @File     :代理服务器的设置.py
# @Software :PyCharm

'''
def use_proxy(proxy_addr,url):
    import urllib.request
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_adder="1.196.105.154:9999"
data=use_proxy(proxy_adder,"http://www.baidu.com")
print(len(data))


import requests

proxies = {
    "http": "http://user:password@127.0.0.1:9743/",
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)
'''
def use_proxy(proxy,url):
    import requests
    proxies = {
        "http": proxy,
    }
    response = requests.get(url=url, proxies=proxies)
    # print(response.status_code)
    response.encoding = response.apparent_encoding
    return response
url = 'https://www.taobao.com'
proxy = '223.242.224.223:9999'
response = use_proxy(proxy,url)
print(response.status_code)
with open('./taobao.html','w',encoding='utf-8') as fp:
    fp.write(response.text)
