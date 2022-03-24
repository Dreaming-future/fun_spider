#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/7 10:47
# @Author   :DKJ
# @File     :图片爬虫实战.py
# @Software :PyCharm


import re
import urllib.request

def craw(url,page):
    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    pat1='<div class="list_cont Left_list_cont  Left_list_cont2">.+?<div class="pages">'
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]
    pat2='data-original="http://(.+?\.jpg)"'
    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imagelist:
        imagename="D:/python/img/"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1


for i in range(1,6):
    url="http://www.win4000.com/meinvtag752_"+str(i)+".html"
    craw(url,i)
