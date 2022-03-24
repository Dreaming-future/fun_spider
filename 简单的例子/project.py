#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/9/22 23:16
# @Author   :DKJ
# @File     :project.py
# @Software :PyCharm

import requests
from lxml import etree
import os

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def Make_dir(filename):
    if not os.path.exists(filename):
        os.makedirs(filename)
        print('文件重新创建')
    else:
        print('文件已创建')


def get_response(url):
    headers ={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36",
        'Referer': 'https://www.haloneuro.com/pages/strength',
    }
    response = requests.get(url,headers=headers)
    return response

def Download_img(list,filename,count):

        # print(list)
    for detail_img_url in list:
        try:
            if detail_img_url !="" and '{width}' not in detail_img_url:
                # print(detail_img_url)
                if(detail_img_url[:2] =='//'):
                    detail_img_url = 'https:' + detail_img_url
                imagename = str(count) + '.jpg'
                img = requests.get(detail_img_url, headers=headers,timeout = 10).content
                with open(filename + '/' + imagename, 'wb') as fp:
                    fp.write(img)
                print(detail_img_url, "下载完成!")
                count += 1
        except Exception as e:
            print(detail_img_url,e, "下载出现异常")

def Download_video(list,filename,count):

    # print(list)
    for detail_video_url in list:

        try:
            imagename = str(count) + '.mp4'
            img = requests.get(detail_video_url, headers=headers,timeout=50).content
            with open(filename + '/' + imagename, 'wb') as fp:
                fp.write(img)
            print(detail_video_url, "下载完成!")
            count += 1
        except Exception as e:
            print(detail_video_url,e, "下载出现异常")

def Download_text(list,filename):
    # print(list)
    for detail_page in list:
        try:
            with open(filename+'/'+'text.txt','a+') as fp:
                fp.write(detail_page)
        except Exception as e:
            print(detail_page)
            print(e, "下载出现异常")

if __name__ == '__main__':
    urls = ['https://www.haloneuro.com/',
            'https://www.haloneuro.com/products/halo-sport-2',
            'https://www.haloneuro.com/collections/frontpage',
            'https://www.haloneuro.com/pages/science',
            'https://www.haloneuro.com/pages/experience',
            'https://www.haloneuro.com/pages/halo-sport-for-musicians',
            'https://www.haloneuro.com/pages/skill',
            'https://www.haloneuro.com/pages/strength',
            'https://www.haloneuro.com/pages/endurance',
            'https://www.haloneuro.com/pages/results',
            'https://www.haloneuro.com/pages/support'
            ]
    Make_dir("html")
    for url in urls:
        response = get_response(url)
        print(response.status_code)
        page_text = response.text
        page_name = url.split('/')[-1]
        try:
            with open('html/'+ page_name+'.html','w',encoding='utf-8') as fp:
                fp.write(page_text)
            print(url,'网页爬取完毕')
        except Exception as e:
            print(url,e)
    # img_filename = "img"
    # video_filename = "video"
    # text_filename = "text"
    # Make_dir(img_filename)
    # Make_dir(video_filename)
    # Make_dir(text_filename)
    # text_list = []
    # img_list = []
    # video_list = []
    # for url in urls:
    #     response = get_response(url)
    #     print(url,response.status_code)
    #     page_text = response.text
    #     tree = etree.HTML(page_text)
    #     img_list += tree.xpath('//img/@src')
    #     img_list += tree.xpath("//img/@data-src")
    #     img_list += tree.xpath('//div[@class="shg-box-vertical-align-wrapper"]/div/@data-bgset')
    # # img_list += ['https://i.shgcdn.com/44966ac5-7541-4473-a515-1727a4f9c1f5/-/format/auto/-/preview/3000x3000/-/quality/lighter/','https://i.shgcdn.com/5d780461-f3e2-45c1-a4f3-00f9157024b0/-/format/auto/-/preview/3000x3000/-/quality/lighter/','https://i.shgcdn.com/bafb4f17-a383-4a73-9954-e949732799bd/-/format/auto/-/preview/3000x3000/-/quality/lighter/','https://i.shgcdn.com/d9f10bf0-05b1-4f64-967a-938762707db4/-/format/auto/-/preview/3000x3000/-/quality/lighter/','https://i.shgcdn.com/44966ac5-7541-4473-a515-1727a4f9c1f5/-/format/auto/-/preview/3000x3000/-/quality/lighter/']
    # # print(img_list)
    # #
    #     video_list += tree.xpath('//video//source[2]/@src')
    # # print(video_list)
    # #
    #     text_list += ['title\n']
    #     text_list += tree.xpath('//h1//text()')
    #     text_list += tree.xpath('//h2//text()')
    #     text_list += tree.xpath('//h3//text()')
    #     text_list += tree.xpath('//h4//text()')
    #     text_list += tree.xpath('//h5//text()')
    #     text_list += tree.xpath('//h6//text()')
    #     text_list += ['超链接a\n']
    #     text_list += tree.xpath('//a//text()')
    #     text_list += ['段落p\n']
    #     text_list += tree.xpath('//p//text()')
    #     text_list += tree.xpath('//span//text()')
    #     text_list += tree.xpath('//button//text()')
    #     text_list += ['列表li\n']
    #     text_list += tree.xpath('//li//text()')
    #
    # img_list += [
    #     'https://i.shgcdn.com/44966ac5-7541-4473-a515-1727a4f9c1f5/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/5d780461-f3e2-45c1-a4f3-00f9157024b0/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/bafb4f17-a383-4a73-9954-e949732799bd/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/d9f10bf0-05b1-4f64-967a-938762707db4/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/44966ac5-7541-4473-a515-1727a4f9c1f5/-/format/auto/-/preview/3000x3000/-/quality/lighter/']
    # img_list += [
    #     'https://cdn.shopifycdn.net/s/files/1/0037/7965/7840/products/Product_Image_Hero_360x.jpg?v=1575913431',
    #     'https://cdn.shopifycdn.net/s/files/1/0037/7965/7840/products/Product_Image_quarter_360x.jpg?v=1575913431',
    #     'https://cdn.shopifycdn.net/s/files/1/0037/7965/7840/products/Product_Image_flat_360x.jpg?v=1575913444',
    #     'https://cdn.shopifycdn.net/s/files/1/0037/7965/7840/products/Product_Image_Side_b34072e1-bc03-4057-bcfd-d9909ce47c6c_360x.jpg?v=1575913456'
    # ]
    # img_list += [
    #     'https://i.shgcdn.com/4b86e4b8-7e63-4a8c-862d-f5b93107982c/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/487557fa-041c-43bb-8a07-67b3b3efb667/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/d44dffe2-2966-4470-adc6-72cd31e24fc1/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/b2e98834-38ef-4a06-8b8f-687a6f98d08a/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/a18e06d9-b3b5-47e7-b9f5-d3a696b2897d/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/50607a0f-5d53-43e6-ae01-e184a9f41af8/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/f367664a-fe91-4657-b1b1-55f4d659a966/-/format/auto/-/preview/3000x3000/-/quality/lighter/',
    #     'https://i.shgcdn.com/93a660ce-fd11-45d0-b2fb-a4ccbc3e0406/-/format/auto/-/preview/3000x3000/-/quality/lighter/'
    # ]
    # count = 0
    # # print(img_list)
    # # Download_img(img_list,img_filename,count)
    # count = 0
    # # print(video_list)
    # # Download_video(video_list,video_filename,count)
    # print(text_list)
    # Download_text(text_list,text_filename)

