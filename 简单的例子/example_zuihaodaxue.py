#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/3/26 11:06
# @Author   :DKJ
# @File     :example_zuihaodaxue.py
# @Software :PyCharm


import  requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r= requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return print("error")

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivlist(ulist, num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print("{0:^10}\t{1:{3}^6}\t{2:^16}".format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivlist(uinfo,20)

main()
