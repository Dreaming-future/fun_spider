# -*- coding: utf-8 -*-
import scrapy
from qiushiPro.items import QiushiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qiushibaike.com/text']

    def parse(self, response):
        # 解析作者的名字+段子内容
        print(response)
        div_list = response.xpath('//div[@id="content"]/div[1]/div[2]/div')
        # print(div_list,"ok")
        all_list = []
        for div in div_list:
            #xpath函数返回的为列表，列表中存放的数据为Selector类型的数据。我们解析到的内容被封装在了Selector对象中，
            # 需要调用extract()函数将解析的内容从Selecor中取出。
            # author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()')[0].extract_first()
            author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a[@class="contentHerf"]/div/span/text()').extract()
            content = '\n'.join(content)

            item = QiushiproItem()
            item['author'] = author
            item['content'] = content

            yield item #提交item到管道文件（pipelines.py）
            # dict = {"作者":author,"内容":content}
            # all_list.append(dict)
            # print(author,content)
            # break
        # return all_list