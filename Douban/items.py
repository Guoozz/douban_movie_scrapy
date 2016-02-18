# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags
import re

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    movie_name = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join,
        )
    movie_director = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        )
    movie_writer = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_type = scrapy.Field()
    movie_date = scrapy.Field()
    movie_rates = scrapy.Field(
        output_processor = MapCompose(int),
        )
    movie_urls = scrapy.Field()
    movie_desc = scrapy.Field(
        output_processor = Join('\n'),
        input_processor = MapCompose(lambda s:re.sub('( |\t|\n)+','',s))
        )
