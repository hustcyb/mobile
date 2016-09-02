# -*- coding: utf-8 -*-

import scrapy
import json
from mobile.loaders import MobileLoader


class PaipaiSpider(scrapy.Spider):
    name = 'paipai'

    def start_requests(self):
        with open('mobiles.json') as file:
            rows = json.load(file)

        for row in rows:
            for index in range(0, 10000):
                number = 10000 * int(row['mobile']) + index 
                number *= 10000
    
                url = 'http://virtual.paipai.com/extinfo/GetMobileProductInfo?mobile=%s&amount=10000&callname=getPhoneNumInfoExtCallback' % number
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        responseText = response.body_as_unicode()
        loader = MobileLoader()
        loader.add_value('mobile', responseText, re = "mobile:'([^']*)'") 
        loader.add_value('province', responseText, re = "province:'([^']*)'")
        loader.add_value('city', responseText, re = "cityname:'([^']*)")
        loader.add_value('isp', responseText, re = "isp:'([^']*)")

        yield loader.load_item()
