# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst,Compose
from w3lib.html import remove_tags
import re

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field(
        output_processor = TakeFirst(),
    )
    director = scrapy.Field(
        input_processor = MapCompose(remove_tags),
    )
    writer = scrapy.Field()
    actor = scrapy.Field()
    types = scrapy.Field()
    date = scrapy.Field()
    update_time = scrapy.Field()
    rates = scrapy.Field(
        output_processor = MapCompose(float),
    )
    urls = scrapy.Field()
    desc = scrapy.Field(
        input_processor = MapCompose(lambda s:re.sub(u'\s+','',s,flags=re.UNICODE)),
        output_processor = Join('\n '),
    )
    
    
