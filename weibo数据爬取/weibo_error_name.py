import requests
from lxml import etree
import pandas as pd
import os
import json



def get_url(name):
    response = requests.get('https://s.weibo.com/user',headers=headers,params={'q':name,"Refer":"weibo_user"})
    tree = etree.HTML(response.text)
    names_url = tree.xpath('//div[@id="pl_user_feedList"]//div[@class="info"]//a//@href') # 找到名字，并且选取第一个
    return names_url

def get_information(name):
    if name not in error_name_lists:
        return
    names_url = get_url(name)
    try:
        response = requests.get('https://weibo.com/ajax/profile/info',headers=headers,params={'custom':names_url[0].split('/')[-1]})
    except Exception as e:
        # print(e)
        error_names.append(name)
        print(name + "未找到")
        # print("已经成功爬取了{}条数据".format(len(information)))

        # information[name]['verified_reason'] = "未找到" if information[name]['verified_reason'] == "" else information[name]['verified_reason']
        # information[name]['description'] = "未找到" if information[name]['description'] == "" else information[name]['description']
        # break
        return
    try:
        info = json.loads(response.text)["data"]["user"]
        information[name] = {"verified_reason":"","description":""}
        verified_reason = info["verified_reason"] if "verified_reason" in info else "无认证"
        description = info["description"] if "description" in info else "无介绍"
        
        information[name]['verified_reason'] = verified_reason
        information[name]['description'] = description
        print("{} 已被爬取认证和介绍 并成功爬取{}条数据".format(name,len(information)))
        # if len(information) % 100 == 0 and len(information) > 100:
        save_csv()
            # time.sleep(180)
    except:
        error_names.append(name)
    
        
    
def save_csv():
    for i in range(len(data)):
        name = data.loc[i,"发布者ID"]
        if name in information.keys():
            data.loc[i,'verified_reason'] = information[name]['verified_reason']
            data.loc[i,'description'] = information[name]['description']
            with open('names.txt','a+') as f:
                f.write('{}\n'.format(name))
        else:
            pass
    data.to_csv('new_weibo_sample_525_5.csv',encoding='utf_8_sig',index=False)
    

from multiprocessing.dummy import Pool

if __name__ == '__main__':
    
    # try:
    path = 'new_weibo_sample_525_4.csv'
    data = pd.read_csv(path)
    
    try:
        with open("error_name.txt", 'r') as f:
            name_lists = f.readlines()
            for i in range(len(name_lists)):
                name_lists[i] = name_lists[i].replace("\n", "")
        error_name_lists = list(set(name_lists))
    except:
        error_name_lists = []

    import time
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',# 伪装成浏览器
        'cookie':'SINAGLOBAL=20037146704.239285.1620219550117; _ga=GA1.2.267774703.1623314703; __gads=ID=2095934ca96ee8e7:T=1623314703:S=ALNI_MYUdC2bauFgWmtwQAyqdNUcPEOqmA; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhXL8pr0Z8U6m2nKrFSaemV5JpX5KMhUgL.Fo-fSKqf1h.0SKn2dJLoIXnLxKqL1h5L12-LxKBLBo.L1hnLxKnLBKML1h.LxK-LB.-L1KMLxKnL1hMLB-2LxK-LBoMLBo2LxK-LBK-LB.BLxK-L1hzLB.zt; ALF=1669260909; SSOLoginState=1637724910; SCF=ApnIF33C4SYo3Za1WDqewVd_-W6yYV6Km39j8z9urK3N_eap8dS43ryH4GYgX6V0MvoYw_fyHcT0rg13ZZ_Gk3E.; SUB=_2A25MmcK-DeThGeNL7lQU-CfPzjSIHXVv7rN2rDV8PUNbmtANLWHCkW9NSO9ONBRdD_Ix-L3IqeBSbpRRXL2Sg6ge; _s_tentry=login.sina.com.cn; Apache=5137753681345.81.1637724912244; UOR=,,login.sina.com.cn; ULV=1637724912251:16:3:3:5137753681345.81.1637724912244:1637125323387',
    }
    params = {}
    
    information = {}
    error_names = []

    pool = Pool(8)
    pool.map(get_information,error_name_lists)
    save_csv()
    
    time.sleep(100)

    pool.map(get_information,list(set(error_names)))
    save_csv()