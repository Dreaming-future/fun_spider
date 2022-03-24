#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/17 18:57
# @Author   :DKJ
# @File     :meizitu_done.py
# @Software :PyCharm

'''
❤️❤️ 背景简介 ❤️❤️
 🎈妹子图:🎈
    有两个:  图片都一样.
    www.meizitu.com 没广告, 一页多张照片. 不好爬
    www.mzitu.com   广告多, 一页一张照片. 有水印,容易爬
    先来简单的，于是爬了www.mzitu.com
 🎈网站分析🎈:
     妹子图几乎每天都更新，
     到现在为止有 140页
     每页24个主题写真，
     每个主题下有几十张照片，每张照片一个网页.
     网页结构简单.用 BeautifulSoup 就可以轻松爬取。
    📌 网站140+页.  每页的网址很有规律 1-140
        只要能获得一个页面里面的数据
        剩下页面的数据只要从1到140 循环.就可以了
        http://www.mzitu.com/page/1
        http://www.mzitu.com/page/2
        http://www.mzitu.com/page/3
        ......
        http://www.mzitu.com/page/140
    📌 每页24个主题. 每个主题一个链接.
        http://www.mzitu.com/87933
        http://www.mzitu.com/87825
        每个主题之间就没什么联系了.
        所有主题的网址就得手动爬下来.
        这里就不能用循环了...
    📌 每个主题诺干张图片. 每张图片一个网址
        http://www.mzitu.com/86819/1
        http://www.mzitu.com/86819/2
        http://www.mzitu.com/86819/3
        单个主题下的图片很有规律
        只要知道这个主题的图片数量就能循环出某主题下所有的网址.
        这个网址 不等于 图片的网址.
        图片网址 需要到每个网页下面匹配出来.
 🎈爬虫步骤：🎈
     整个妹子图所有主题的网址.            get_page1_urls
     某主题下第一张照片地址               get_img_url
     某主题的照片数                       get_page_num
     用循环获取某主题下所有照片地址       get_img_url
     获取各个主题的主题名字               get_img_title
     下载所有主题下的所有照片             download_imgs
'''

# ❤️❤️ ↓↓↓ 0: 依赖模块 ↓↓↓ ❤️❤️


import urllib.request          # 获取网页内容
from bs4 import BeautifulSoup  # 解析网页内容
import re                      # 正则式模块.
import os                      # 系统路径模块: 创建文件夹用
import socket                  # 下载用到
import time                    # 下载用到

# ❤️❤️ ↓↓↓ 获取整个妹子网所有的主题 ↓↓↓ ❤️❤️


def get_page1_urls():          # 定义一个函数
    page1_urls = []            # 定义一个数组,来储存所有主题的URL
    for page in range(1, 2):
        # 1-140. 整个妹子图只有140页,注意下面缩进内容都在循环内的!
        url = 'http://www.mzitu.com/page/' + str(page)
        request = urllib.request.Request(url)
        # 制作请求头了. 140页 每页都请求一遍. 自然就能获取到每页下的24个主题了
        html = urllib.request.urlopen(request, timeout=20).read()
        # read 就是读取网页内容并储存到 html变量中.
        soup = BeautifulSoup(html, 'lxml')
        # 把下载的网页.结构化成DOM, 方便下面用 find 取出数据
        lis = soup.find('ul', {'id': 'pins'}).find_all('li')
        # 找到 id 为pins 这个列表下面的 每个列 就找到每个页面下的 24个主题了
        for li in lis:
            # 遍历每页下面的24个主题 (也就是24个li)
            page1_urls.append(li.find('a')['href'])
            # 把每个主题的地址. 添加到page1_urls 这个数组里面.
        # print(page1_urls)
        # # 显示网址. 测试用. 循环140次. 这样就获得了所有主题的网址了
    return page1_urls

# ❤️❤️ ↓↓↓ 自动获取某主题的照片数量 ↓↓↓ ❤️❤️
# 进入某个主题, 然后分析底部的 导航条.
# 导航条格式: 上一组 1 2 3 4 ... 64 下一组
# 很多按钮.每个按钮都是一个<a>元素.
# 倒数第二个<a>元素 这里也就是64 就是照片数量!

def get_page_num(page1_url):        # 参数 page1_url 不一定要外界传入的. 可以给函数里面用的.
    request = urllib.request.Request(page1_url)
    try:
        html = urllib.request.urlopen(request, timeout=20).read()
    except:
        try:
            html = urllib.request.urlopen(request, timeout=20).read()
        except:
            return None
            # 这个函数会重复请求两次. 如果两次都超时就放弃.
    soup = BeautifulSoup(html, 'lxml')
    try:
        page_num = soup.find('div', {'class': 'pagenavi'}).find_all('a')[-2].find('span').get_text()
    except:
        return None
    return int(page_num)

# ❤️❤️ 三: 获取某主题下第一张照片的URL. ❤️❤️
# 结合上面的照片数量. 就能获取到某主题下的所有照片链接了.


def get_img_url(url):
    request = urllib.request.Request(url)
    try:
        html = urllib.request.urlopen(request, timeout=20).read()
    except:
        try:
            html = urllib.request.urlopen(request, timeout=20).read()
        except:
            return None
    soup = BeautifulSoup(html, 'lxml')
    try:
        img_url = soup.find(
            'div', {'class':
                    'main-image'}).find('p').find('a').find('img')['src']
    except:
        return None
    return img_url

def get_img_urls(page1_url):
    page_num = get_page_num(page1_url)
    # 这里就用到了 上面的 get_page_num 这个函数了.
    if page_num is None:
        return None
    img_urls = []
    # 定义一个数组 来储存该主题下的 所有照片的 URL
    for page in range(1, page_num + 1):
        url = page1_url + '/' + str(page)
        # 实际照片的链接地址 就是主题的链接 + / + 数量
        img_url = get_img_url(url)
        # 这里用到了 get_img_url 这个函数. 可以获取该主题下的第一张照片.
        # 现在是在循环里面. 循环次数就是 该主题的照片数量+1
        if img_url is None:
            return None
        else:
            img_urls.append(img_url)
        # 把获取到的 url 添加到 img_urls 这个数组里.
        # 这样循环下来 img_urls 数组里面就有该主题下的所有照片地址了
    return img_urls

# ❤️❤️ 五: 获取某主题名称,创建本地文件夹用 ❤️❤️


def get_img_title(page1_url):
    request = urllib.request.Request(page1_url)
    try:
        html = urllib.request.urlopen(request, timeout=20).read()
    except:
        try:
            html = urllib.request.urlopen(request, timeout=20).read()
        except:
            return None
    soup = BeautifulSoup(html, 'lxml')
    # <h2 class="main-title">古典气质型美女施诗 顶级美腿加酥胸圆臀火辣身材性感十足</h2>
    title = soup.find('h2', {'class': 'main-title'}).get_text()
    # 下面两行是异常分析..
    removeSign = re.compile(r'[\/:*?"<>|]')
    # re 就是正则表达式模块
    # re.compile 把正则表达式封装起来. 可以给别的函数用. ()里面的才是真的 表达式.
    # r'[\/:*?"<>|]'
    # [] 表示一个字符集;  \对后面的进行转义 英文/是特殊符号; 其他的是正常符号.
    title = re.sub(removeSign, '', title)
    # re.sub 在字符串中 找到匹配表达式的所有子串. 用另一个进行替换.这里用'' 就是删除的意思.
    # 就是说 删除标题里面的 /:*?"<>| 这些符号.
    # 英文创建文件夹时候 不能有特殊符号的!!!
    return title

# ❤️❤️ 六: 定义下载某主题所有图片的函数 ❤️❤️
# 下载肯定要创建文件夹.要用到路径.这就需要 os 模块了.
# 我们把照片 建立个文件夹 下载到 脚本运行的目录下
# os.path模块主要用于文件的属性获取，经常用到，以下是该模块的几种常用方法
# print(os.getcwd())                 # 获取并输出当前脚本所在的目录.
# os.mkdir('./妹子图')               # 在当前文件夹下 建立 妹子图 文件夹.
# os.rmdir('./妹子图')               # 在当前文件夹下 删除 妹子图 文件夹.
# if os.path.exists('./妹子图'):     # 判断当前文件夹 是否存在   妹子图这个文件夹
# if not os.path.exists('./妹子图'): # 判断当前文件夹 是否不存在 妹子图这个文件夹
# 本项目我们先判断当前脚本文件夹 是否已经有妹子图这个文件夹存在.
# 如果不存在那就新建一个妹子图文件夹.
# 再判断妹子图文件夹下 有没有对应的子文件夹存在.


def download_imgs(page1_url):
    img_urls = get_img_urls(page1_url)
    if img_urls is None:
        return None
    if not os.path.exists('./妹子图'):
        os.mkdir('./妹子图')
    title = get_img_title(page1_url)
    if title is None:
        return
    local_path = './妹子图/' + title
    if not os.path.exists(local_path):
        try:
            os.mkdir(local_path)
        except:
            pass
    if img_urls is None or len(img_urls) == 0:
        return
    else:
        print('--开始下载' + title + '--')
        for img_url in img_urls:
            img_name = os.path.basename(img_url)
            print('正在下载 ' + img_name)
            print('from ' + img_url)
            socket.setdefaulttimeout(10)
            try:
                urllib.request.urlretrieve(img_url, local_path + '/' + img_name)
            except:
                print('下载' + img_name + '失败')
        print('--' + title + '下载完成--')


# ❤️❤️ 七: 下载所有主题的图片 ❤️❤️


def craw_meizitu():
    page1_urls = get_page1_urls()
    # 这里用到了 第一个函数. 也就是获取所有主题的 URL.
    if page1_urls is None or len(page1_urls) == 0:
        return
    else:
        for page1_url in page1_urls:
            # 循环第六步 来下载所有主题的URL
            download_imgs(page1_url)


def main():
    craw_meizitu()
if __name__ == '__main__':
    main()