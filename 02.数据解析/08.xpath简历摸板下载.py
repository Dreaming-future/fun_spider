#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/15 9:47
# @Author   :DKJ
# @File     :08.xpath简历摸板下载.py
# @Software :PyCharm

import  requests
from lxml import etree
import os
first_url = 'http://sc.chinaz.com/jianli/yingwenjianli.html'
url = 'http://sc.chinaz.com/jianli/yingwenjianli_%s.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
if not os.path.exists('jianli'):
    os.makedirs('jianli')

start_page = int(input('enter the start page:'))
end_page = int(input('enter the end page:'))

for page in range(start_page,end_page+1):
    print('正在打印第%d页的数据'%page)
    if page == 1:
        new_url = first_url
    else:
        new_url = format(url%page)
    response = requests.get(url=new_url,headers=headers)
    page_text = response.text
    print(response.encoding)
    tree = etree.HTML(page_text)
    url_list = tree.xpath('//div[@id="container"]//a/@href')
    # print(url_list)
    for detail_url in url_list:
        detail_response = requests.get(url= detail_url,headers=headers)
        detail_page_text = detail_response.text
        detail_tree = etree.HTML(detail_page_text)
        name = detail_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
        # name = name.encode('iso-8859-1').decode('gbk')
        each_url = detail_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li/a/@href')[0]
        try:
            each_response = requests.get(each_url,headers=headers)
            each = each_response.content
            with open('jianli/'+name+'.rar','wb') as fp:
                fp.write(each)
            print(each_url,name,"下载成功")
        except Exception as e:
            print(e, "下载出现异常")

print("--------------------------------over!!!--------------------------------")