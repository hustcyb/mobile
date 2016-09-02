# -*- coding: utf-8 -*-

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from mobile.items import Mobile


class MobileLoader(ItemLoader):
    default_item_class = Mobile
    default_input_processor = MapCompose(unicode.strip)
    default_output_processor = TakeFirst()
