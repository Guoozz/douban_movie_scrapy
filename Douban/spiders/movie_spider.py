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
        "http://movie.douban.com/subject/20326665/?from=showing"
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'movie\.douban\.com/subject/[0-9]+(/\?from=.+|/)?$',)),
             callback='parse_movie',process_links='filter_links',follow=True),
    )

    #开始request,初始化一些参数
    def start_requests(self):
        self.visited_links = set()
        self.attr_xpath = set()
        with open('douban_movie.txt',mode='r') as f:
            for line in f:
                self.attr_xpath.add(tuple(line.split(None,2)))
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def filter_links(self,links):
        filtered_links = set(link for link in links
                             if link not in self.visited_links)
        self.visited_links.update(filtered_links)
        return filtered_links
        
    def parse_movie(self,response):
        item = DoubanItem()

        for attr,xpath_pattern in self.attr_xpath:
            item[attr] = ','.join(response.xpath(xpath_pattern).extract())

        yield item
       

                   
