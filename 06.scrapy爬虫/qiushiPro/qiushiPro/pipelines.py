# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class QiushiproPipeline(object):
    fp = None

    # 开始爬虫时，执行一次
    def open_spider(self, spider):
        print('爬虫开始')
        self.fp = open('./data.txt', 'w')

    def process_item(self, item, spider):
        self.fp.write(item['author'] + ':' + item['content'] + '\n')
        return item

    # 结束爬虫时，执行一次
    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束')
