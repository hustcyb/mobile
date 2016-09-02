# -*- coding: utf-8 -*-

import scrapy
import json
from mobile.items import Mobile
from mobile.loaders import MobileLoader


class Shouji360Spider(scrapy.Spider):
    name = 'shouji360'

    def start_requests(self):
        with open('mobiles.json') as file:
            rows = json.load(file)

        for row in rows:
            for index in range(0, 10000):
                number = 10000 * int(row['mobile']) + index 
                number *= 10000
    
                url = 'http://cx.shouji.360.cn/phonearea.php?number=%s' % number
                request = scrapy.Request(url, self.parse)
                
                item = Mobile()
                item['mobile'] = number
                request.meta['item'] = item

                yield request

    def parse(self, response):
        responseText = response.body_as_unicode()
        responseData = json.loads(responseText)

        if responseData['code'] == 0:
            item = response.meta['item']
            loader = MobileLoader(item)

            data = responseData['data']
            loader.add_value('province', data['province'])
            loader.add_value('city', data['city'])
            loader.add_value('isp', data['sp'])

            yield loader.load_item()
