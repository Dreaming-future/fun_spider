#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020/7/24 17:23
# @Author   :DKJ
# @File     :csv存储.py
# @Software :PyCharm


import csv
with open ('../data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name','age'])
    writer.writerows([['10001' , 'Mike' , 20],[' 10002 ',' Bob ', 22],['10003 ',']ordan ', 21]])
#     writer = csv.writer(csvfile,delimiter=' ')
#     writer.writerow ([' id ', ' name ',' age'])
#     writer. writerow( [' 10001' , 'Mike' , 20])
#     writer .writerow([' 10002 ',' Bob ', 22])
#     writer.writerow(['10003 ',']ordan ', 21])
# 字典存储
import csv
with open (' data.csv ','w') as csvfile:
    fieldnames = ['id','name' ,'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer. writeheader()
    writer.writerow({'id':'10001', 'name':'Mike','age': 20})
    writer.writerow({'id':'10002','name': 'Bob', 'age': 22})
    writer.writerow({'id':'10003','name' : 'Jordan','age': 21})

import csv

with open('../data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)