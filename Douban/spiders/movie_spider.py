#! /usr/bin/python
# -*- coding:utf-8 -*-

from scrapy import Spider,Request
from Douban.items import DoubanItem
from scrapy.exceptions import IgnoreRequest

class MovieSpider(Spider):
    name='douban_movie'
    allowed_domains = ['douban.com']
    start_urls=[
        "http://movie.douban.com/subject/20326665/?from=showing"
    ]

    #xpath save in douban_movie.txt
    pattern_file_name = 'douban_movie.txt'
    urls_pattern = '//dt/a/@href'
    visited_url = set()
    
    def attr_xpath_pattern(self):
        with open(self.pattern_file_name) as f:
            for line in f:
                yield tuple(line.strip().split(' '))
                
    def parse(self,response):
        item = DoubanItem()

        for attr,xpath_pattern in self.attr_xpath_pattern():
            item[attr] = ','.join(response.xpath(xpath_pattern).extract()).encode('utf-8')

        yield item

        #防止request重复的url
        douban_urls = set(response.xpath(self.urls_pattern).extract())
        filter_urls = (url for url in douban_urls if url not in self.visited_url)

        for url in filter_urls:
            yield Request(url,self.parse)
            
