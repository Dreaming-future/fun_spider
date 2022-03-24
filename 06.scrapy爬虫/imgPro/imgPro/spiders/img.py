# -*- coding: utf-8 -*-
import scrapy
from imgPro.items import ImgproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            # 使用伪属性
            src = div.xpath('./div/a/img/@src2').extract_first()
            # print(src)
            item = ImgproItem()
            item['src'] = src
            yield item