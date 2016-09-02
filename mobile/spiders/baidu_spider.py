# -*- coding: utf-8 -*-

import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu' 
    start_urls = [
        'http://baike.baidu.com/link?url=CStXnd4Rw2C4HE6zwbQRGDktgctuuPlR5zrBQoa5PQ86cF5MlIq3XBxhXIVTIaD-Z_KudcjCtQ-StlHdEaspmK'
    ]

    def parse(self, response):
        mobiles = []
        for mobile in response.xpath(u"//div[@class='para'][not(starts-with(text(),'未知号段：')) and not(starts-with(text(),'4G号段：'))]//text()").re(r'\b\d{3}\b'):
            item = {}
            mobile = int(mobile)
            mobiles.append(mobile)

        mobiles.sort()
        for mobile in mobiles:
            yield { 'mobile': mobile }
