#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/17 16:09
# @Author   :DKJ
# @File     :github.py
# @Software :PyCharm

import requests
from lxml import etree
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
#创建会话对象,该会话对象可以调用get和post发起请求
session = requests.Session()
#使用会话对面对登录页面发起请求
page_text = session.get(url='https://github.com/login',headers=headers).text
#解析出动态的taken值
tree = etree.HTML(page_text)
t = tree.xpath('//*[@id="login"]/form/input[1]/@value')[0]
# print(t)
#指定模拟登录请求的url
url = 'https://github.com/session'
#参数封装（处理动态taken值）
data = {
'commit':'Sign in',
'authenticity_token':t,
# 'ga_id':'811320128.1581672787',
'login':'Dreaming-future',
'password':'a13790699906',
'webauthn-support':'supported',
# 'webauthn-iuvpaa-support':'supported',
# 'return_to':'',
# 'required_field_224d':'',
# 'timestamp':'1594981742492',
# 'timestamp_secret':'32c3b1bf05442c7d276a0db5c28786c02db2073f3d48c6a407a1a6a5aae889ae',
}

page_text = session.post(url,headers=headers,data=data).text

with open('./git.html','w',encoding='utf-8') as fp:
    fp.write(page_text)