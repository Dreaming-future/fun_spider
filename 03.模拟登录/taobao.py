#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/4/4 16:40
# @Author   :DKJ
# @File     :taobao.py
# @Software :PyCharm

# CrowTaobaoPrice.py
import requests
import re


def getHTMLText(url,header):
    try:
        r = requests.get(url,headers=header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt,goods):
    tplt = "{:4}\t{:8}\t{:16}"
    title = ["序号","价格","商品名称      "+goods,'\n']
    with open('taobao.csv','a') as fp:
        fp.write(','.join(title))
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        glist = [str(count),g[0],g[1],"\n"]
        with open('taobao.csv', 'a', encoding="gbk") as fp:
            fp.write(','.join(glist))
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = input("请输入查询的关键字:")
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    header={
        "Cookie":'mt=ci%3D-1_0; _m_h5_tk=17b42a151f8782f03a3470228baeecb1_1585999095706; _m_h5_tk_enc=e0b2a2e093c5494391d61e18bcfbc3b8; cna=KLrBFssyz2cCAXFA3XIp6OB9; cookie2=5ee6957c48d9b7075b186709660613cf; t=e958c097b5892b4d1cb36684a2a2b0cb; _tb_token_=f8103e3e7d753; UM_distinctid=171445ae6fe314-0f48c191f7cb6d-f313f6d-144000-171445ae70137d; thw=cn; _samesite_flag_=true; v=0; sgcookie=E6VaVXzX8J3xCjyq1D2Kq; unb=2784907342; uc3=nk2=2WdxW4SElfvb2GUO&id2=UU8A4oebjSTfRQ%3D%3D&vt3=F8dBxdAXvWSGk0eOkDM%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; csg=4470acf3; lgc=%5Cu5475%5Cu5475%5Cu968F%5Cu610F%5Cu800C%5Cu4E3A; cookie17=UU8A4oebjSTfRQ%3D%3D; dnk=%5Cu5475%5Cu5475%5Cu968F%5Cu610F%5Cu800C%5Cu4E3A; skt=8f1df18d73ec2356; existShop=MTU4NjAwNDczMw%3D%3D; uc4=nk4=0%4024HDYBPKTvhJxHohq6oXbVmJR2EBUAE%3D&id4=0%40U22Hvy88sTsAmT9cCm5PI7902dgf; tracknick=%5Cu5475%5Cu5475%5Cu968F%5Cu610F%5Cu800C%5Cu4E3A; _cc_=UIHiLt3xSw%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E4%B8%BA26; _nk_=%5Cu5475%5Cu5475%5Cu968F%5Cu610F%5Cu800C%5Cu4E3A; cookie1=W5%2Ff1j6ojGJqwEr%2BqBw9fO35IduYJQ48j0TbkhVYXlE%3D; enc=65L%2B6jivkvksU0RA37cUzF02fR67KcEVSYpV7Wtkk6NrNXAbO6rQLikQXyMHBkxYuiHU3GGZZhffjWfQh28CIQ%3D%3D; JSESSIONID=2320FEC7A072EFF3587D815DBC410283; tfstk=cO2VB0msutBVd9i4HvDZcSBmKCEAZ90iRLoEiWor1lxCM0hcio8tqgTt4cudEjf..; l=dBIyvOoVQXSrSzQLBOCZlurza77OSIRYMuPzaNbMi_5BO6YsfuQOo1hGtFv6VjWftxLB4cjscSv9-etkZQDmndK-g3fPaxDc.; isg=BMHBPi0-e5hMEJes26z199-Z0A3b7jXgCeDXxCMWvUgnCuHcaz5FsO8I6H5MWs0Y; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTUPOTyxRWkLg%3D%3D&tag=8&lng=zh_CN; mt=ci=25_1',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url,header)
            # print(html)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList,goods)

main()