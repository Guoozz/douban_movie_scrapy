#! /usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from Douban.items import DoubanItem
from scrapy.loader import ItemLoader

class MovieSpider(CrawlSpider):
    name='douban_movie'
    allowed_domains = ['douban.com']
    start_urls=[
        "http://movie.douban.com",
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'movie\.douban\.com/subject/[0-9]+(/\?from=.+|/)?$',)),
             callback='parse_movie',follow=True),
    )

    def parse_movie(self,response):
        
        loader = ItemLoader(item=DoubanItem(),response=response)
        
        for attr,xpath_pattern in self.settings.getdict('ATTR_XPATH').items():
            loader.add_xpath(attr,xpath_pattern)

        return loader.load_item()
       

                   
