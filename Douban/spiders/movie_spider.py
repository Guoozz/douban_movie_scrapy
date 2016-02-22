#! /usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from Douban.items import DoubanItem,RateItem
from scrapy.loader import ItemLoader
import re

class MovieSpider(CrawlSpider):
    name='douban_movie'
    allowed_domains = ['douban.com']
    start_urls=[
        "http://movie.douban.com",
        "http://movie.douban.com/subject/24875409/?from=tag",
        "http://www.douban.com/tag/2016/?focus=movie",
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'movie\.douban\.com/subject/[0-9]+(/\?from=.+|/)?$',)),
             callback='parse_movie',follow=True),
    )
    error_403_count = 0

    def parse_movie(self,response):
        
        loader = ItemLoader(item=DoubanItem(),response=response)
        
        for attr,xpath in self.settings.getdict('INFO_XPATH').items():
            loader.add_xpath(attr,xpath)

        s = response.xpath('//div[@id="info"]').extract_first()
        for attr,regex in self.settings.getdict('RE').items():
            loader.add_value(attr,re.findall(regex,s))
            
        loader.add_value('url',response.url)
        loader.add_value('rate',self.parse_rate(response))

        return loader.load_item()

    def parse_rate(self,response):

        loader = ItemLoader(item = RateItem(),response=response)
        
        for attr,xpath in self.settings.getdict('RATE_XPATH').items():
            loader.add_xpath(attr,xpath)

        return loader.load_item()

                   
