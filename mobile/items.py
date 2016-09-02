# -*- coding: utf-8 -*-

import scrapy


class Mobile(scrapy.Item):
    mobile = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    isp = scrapy.Field()
