#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/13 22:06
# @Author   :DKJ
# @File     :05.requests_yaojian.py
# @Software :PyCharm

import requests
import json
if __name__ == '__main__':
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        # 定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    id_list=[]
    all_data_list = []
    for i in range(1,6):
        page = str(i)
        data = {
            'on':'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
            'Expression': '',
        }
        respsonse = requests.post(url= url,headers=headers,data=data)

        json_ids=respsonse.json()
        for dict in json_ids['list']:
            id_list.append(dict['ID'])

    post_url= 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(post_url,headers=headers,data=data).json()
        all_data_list.append(detail_json)

    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp,ensure_ascii=False)
    print("OVER!!!")

'''
import requests
from fake_useragent import UserAgent
ua = UserAgent(use_cache_server=False,verify_ssl=False).random
headers = {
    'User-Agent':ua
}
url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
pageNum = 3
for page in range(3,5):
    data = {
        'on': 'true',
        'page': str(page),
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }
    json_text = requests.post(url=url,data=data,headers=headers).json()
    all_id_list = []
    for dict in json_text['list']:
        id = dict['ID']#用于二级页面数据获取
        #下列详情信息可以在二级页面中获取
        # name = dict['EPS_NAME']
        # product = dict['PRODUCT_SN']
        # man_name = dict['QF_MANAGER_NAME']
        # d1 = dict['XC_DATE']
        # d2 = dict['XK_DATE']
        all_id_list.append(id)
    #该url是一个ajax的post请求
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in  all_id_list:
        post_data = {
            'id':id
        }
        response = requests.post(url=post_url,data=post_data,headers=headers)
        if response.headers['Content-Type'] == 'application/json;charset=UTF-8':
            #print(response.json())
            #进行json解析
            json_text = response.json()
            print(json_text['businessPerson'])
'''