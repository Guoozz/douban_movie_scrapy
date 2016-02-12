#! /usr/bin/python
# -*- coding:utf-8 -*-

from scrapy import Request
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from Douban.items import DoubanItem

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

    #开始request,初始化一些参数
    def start_requests(self):
        self.attr_xpath = self.settings.get('ATTR_XPATH',None)
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
        
    def parse_movie(self,response):
        item = DoubanItem()

        for attr,xpath_pattern in self.attr_xpath.items():
            item[attr] = response.xpath(xpath_pattern).extract()

        yield item
       

                   
