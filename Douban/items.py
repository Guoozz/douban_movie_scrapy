# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst,Compose
from w3lib.html import remove_tags
import re

def remove_blanks(s):
    return re.sub('\s+','',s)

def remove_percent(s):
    return re.sub('%','',s)

def split_slash(s):
    return s.split('/')

class DoubanItem(scrapy.Item):

    #TakeFisrt type:class
    #override __call__
    name = scrapy.Field(
        output_processor = TakeFirst(),
    )
    
    director = scrapy.Field(
        input_processor = MapCompose(remove_tags),
    )
    

    desc = scrapy.Field(
        input_processor = MapCompose(remove_blanks),
        output_processor = Join('\n '),
    )


    alias = scrapy.Field(
        input_processor = Compose(TakeFirst(),remove_tags,),
        output_processor = Compose(
            TakeFirst(),
            remove_blanks,
            split_slash,
        )
    )

    language = scrapy.Field(
        input_processor = Compose(TakeFirst(),remove_tags,),
        output_processor = Compose(
            TakeFirst(),
            remove_blanks,
            split_slash,
        )
    )
    
    length = scrapy.Field(
        output_processor = Compose(
            TakeFirst(),
            remove_blanks,
            split_slash,
        )
    )

    region = scrapy.Field(
        input_processor = Compose(TakeFirst(),remove_tags,),
        output_processor = Compose(
            TakeFirst(),
            remove_blanks,
            split_slash,
        )
    )
    
    rate = scrapy.Field(
        output_processor = TakeFirst(),
    )
    writer = scrapy.Field()
    actor = scrapy.Field()
    types = scrapy.Field()
    date = scrapy.Field()
    update_time = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    
class RateItem(scrapy.Item):
    num = scrapy.Field(
        output_processor=Compose(TakeFirst(),int),
    )
    average = scrapy.Field(
        output_processor=Compose(TakeFirst(),float)
    )
    stars = scrapy.Field(
        output_processor=MapCompose(remove_percent,float),
    )
