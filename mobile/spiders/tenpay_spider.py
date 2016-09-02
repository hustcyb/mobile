# -*- coding: utf-8 -*-

import scrapy
import json
from mobile.loaders import MobileLoader


class TenpaySpider(scrapy.Spider):
    name = 'tenpay'

    def start_requests(self):
        with open('mobiles.json') as file:
            rows = json.load(file)

        for row in rows:
            for index in range(0, 10000):
                number = 10000 * int(row['mobile']) + index 
                number *= 10000
    
                url = 'http://life.tenpay.com/cgi-bin/mobile/MobileQueryAttribution.cgi?chgmobile=%s' % number
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        loader = MobileLoader(selector = response)
        loader.add_xpath('mobile', '//chgmobile/text()') 
        loader.add_xpath('province', '//province/text()')
        loader.add_xpath('city', '//city/text()')
        loader.add_xpath('isp', '//supplier/text()')

        yield loader.load_item()
