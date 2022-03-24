#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/11 17:54
# @Author   :DKJ
# @File     :CookieJar.py
# @Software :PyCharm

import urllib.request
import urllib.parse
import http.cookiejar
url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q'
postdata=urllib.parse.urlencode(
    {
        "username":"weisuen","password":"aA123456"
    }).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML，像Gecko) Chrome/83.0.4103.116 Safari/537.36')
