#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2021/7/26 12:58
# @Author   :DKJ
# @File     :comment.py
# @Software :PyCharm


from requests import RequestException

def get_page(url,headers,proxy=None):
    try:
        response = requests.get(url, headers=headers,proxies=proxy)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None

def get_blog_url_list(url ,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}):
    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//a/@href')
    # print(li_list)
    # print(li_list)
    url_list = []
    for old_url in li_list:
        if 'article' in old_url and 'category' not in old_url and url.split('/')[-1] in old_url:
            url_list.append(old_url)
    return url_list
#
# def parse_page(url):
#     text = requests.get(url)
#     print(text)
#
# # def comment(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}):
#
#
#
# url_list = get_url_list(url)
# print(len(url_list))
# for url in url_list:
#     print(url)
from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.chrome.options import Options
import requests
from json import loads
import random
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
           "Host": "blog.csdn.net"
           }
def write_commented_url(url,path = 'commented_url.txt'):
    f = open(path,'a+')
    f.write(url+'\n')
    f.close()
def get_commented_url(path = 'commented_url.txt'):
    commented_url = [] # 已经评论的文章，最好不要二次评论
    f = open(path,'r')
    url_list = f.readlines()
    print(url_list)
    for url in url_list:
        url = url.replace('\n','')
        commented_url.append(url)
    f.close()
    return commented_url
def get_url1(start_page = 0,end_page = 50):
    params = {
        "page": str(start_page),
        # 可以修改pageSize的值
        "pageSize": str(end_page),
        # "child_channel":
    }
    # topics = ["c/c++","java","javascript","php","python","人工智能","区块链",
    #           "大数据","移动开发","嵌入式","开发工具","数据结构与算法","测试","游戏","网络","运维"]
    topics = ["c/c++","python","人工智能","大数据","数据结构与算法","区块链","javascript","开发工具"]
    topics = ["c/c++", "python", "人工智能", "大数据"]
    # params["child_channel"] = random.choice(topics)
    # print(params)
    url_set = set('')
    all_url = "https://blog.csdn.net/phoenix/web/blog/hotRank/"  # 领域内容榜
    for topic in topics:
        params["child_channel"] = topic
        # print(params)
        r = requests.get(all_url, headers=headers, params=params)
        # print(r.text)
        # print(loads(r.text))
        datas = loads(r.text)["data"]
        # print(datas)

        print("---------- 这次领域内容榜的主题是" + params['child_channel']+"----------")

        for data in datas:
            url = data["articleDetailUrl"]
            # print(data["nickName"],
            #       data["articleTitle"],
            #       url,
            #       "热度为" + data["pcHotRankScore"]
            #       )
            # url_list.append(url)
            url_set.add(url)
        print("---------- 领域内容榜的主题" + params['child_channel'] + "爬取完毕----------")
        print("\n\n")
    return url_set
def get_url2(start_page = 0,end_page = 50):
    params = {
        "page": str(start_page),
        # 可以修改pageSize的值
        "pageSize": str(end_page),
    }
    url_set = set('')
    all_url = "https://blog.csdn.net/phoenix/web/blog/hotRank/"  # 领域内容榜
    r = requests.get(all_url, headers=headers, params=params)
    datas = loads(r.text)["data"]

    print("----------  正在爬取全站综合热榜 ----------")
    for data in datas:
        url = data["articleDetailUrl"]
        url_set.add(url)
    print("----------  全站综合热榜爬取完毕 ----------")
    print("\n\n")
    return url_set
def comment_blog(comments,url_set,commented_url,total = 0, end = 100):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
    driver = webdriver.Chrome(options=chrome_options,executable_path='C:/bin/chromedriver.exe')
    # driver.get("https://www.baidu.com/")
    print(driver.title)
    for url in url_set:
        if url not in commented_url:
            comment = random.choice(comments)
            driver.get(url)
            try:
                driver.find_element_by_id('is-like-imgactive').click()  # 点赞
            except:
                driver.find_element_by_id('is-like-img').click()
            driver.find_element_by_id('comment_content').clear()  # 找到评论框
            driver.find_element_by_id('comment_content').send_keys(comment)  # 加载评论
            time.sleep(3)
            try:
                driver.find_element_by_css_selector("[class='btn btn-sm btn-comment']").click() # 点击评论
            except:
                driver.find_element_by_css_selector("[class='bt-comment-show']").click()
            finally:
                print(url + ' 已经评论和点赞','评论的内容是: ' + comment)
            write_commented_url(url)
            total += 1
            if total % 10 == 0:
                print('已经评论了 {} 篇文章'.format(total))
            if total == end:
                print('今天评论上限，请试后再确定是否继续评论')
                break
            if total % 20 == 0:
                time.sleep(1800)
            elif total % 50 == 0:
                time.sleep(2700)
            else:
                using_time = random.randint(120,360)
                time.sleep(using_time)
                # time.sleep(5)
    driver.quit()


def main():
    # url = 'https://blog.csdn.net/KIK9973'
    # blog_url = get_blog_url_list(url)
    # print(blog_url)
    # url_set = set(blog_url)
    url_set1 = get_url1(start_page= 0,end_page= 30)
    url_set2 = get_url2(start_page = 0,end_page = 30)
    url_set = ('')
    url_set = url_set1 | url_set2
    print("这次爬取到的评论的网站个数为",len(url_set))
    commented_url = get_commented_url()
    # return
    comments = ['好文，受益匪浅，点赞支持，欢迎回访！',
                '太精辟了啊，竖起我的大拇指！希望互相关注一波！',
                '点赞博主文章，大佬牛批，写的很详细，欢迎回访',
                '内容详细，结构清晰，学到了，欢迎回访哦！',
                '学习佳作，顺手点赞与关住,期待大佬回访！',
                '不错的文章，受益匪浅，欢迎回访',
                '写的好，很nice,期待大佬回访！',
                '支持大佬，原创不易，欢迎回访',
                '期待你更多好的作品，加油哦',
                '太精辟了啊，竖起我的大拇指！希望互相关注一波！',
                '好文，支持大佬，期待大佬也来指点一下我的博文。',
                '好文，已收藏，大佬分析的很到位，明白了很多，大赞！（￣ˇ￣)，大佬有兴趣也可以看下我的博客哈',
                '博主写的非常清晰啊，对我很有帮助，谢谢啦，我也写了一些，欢迎回访',
                '膜拜大佬的技术,来我博客指点江山吧！',
                '写的真清晰，学到了，我也有一些好文章，欢迎回访',
                '给大佬递茶祝上热榜 以三连 望回访',
                ]

    comment_blog(comments,url_set,commented_url,0,100)

if __name__ == '__main__':
    main()

