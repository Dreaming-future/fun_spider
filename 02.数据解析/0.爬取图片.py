#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/14 18:07
# @Author   :DKJ
# @File     :0.爬取图片.py
# @Software :PyCharm


import requests
if __name__ == '__main__':
    Headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    url = 'http://pic.netbian.com/uploads/allimg/200629/230511-1593443111f136.jpg'
    imgae_data = requests.get(url=url,headers=Headers).content

    with open('picture.jpg','wb') as fp:
        fp.write(imgae_data)