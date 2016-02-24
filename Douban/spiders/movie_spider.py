#! /usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from Douban.items import DoubanItem,RateItem
from scrapy.loader import ItemLoader
from urlparse import urljoin
import re

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
    image_base_url = 'http://img3.doubanio.com/view/photo/photo/public/'
    
    def parse_movie(self,response):
        
        loader = ItemLoader(item=DoubanItem(),response=response)
        
        for attr,xpath in self.settings.getdict('INFO_XPATH').items():
            loader.add_xpath(attr,xpath)

        s = response.xpath('//div[@id="info"]').extract_first()
        for attr,regex in self.settings.getdict('RE').items():
            loader.add_value(attr,re.findall(regex,s))
            
        image_urls = self._get_urls(self.image_base_url,urljoin,
                                    response.xpath('//div[@id="mainpic"]/a/img/@src').extract(),
                                    lambda s:s.split('/')[-1],
        )

        loader.add_value('image_urls',image_urls)
        loader.add_value('rate',self.parse_rate(response))
        loader.add_value('url',response.url)
        
        return loader.load_item()

    def parse_rate(self,response):

        loader = ItemLoader(item = RateItem(),response=response)
        
        for attr,xpath in self.settings.getdict('RATE_XPATH').items():
            loader.add_xpath(attr,xpath)

        return loader.load_item()
            
    def _get_urls(self,base_url,combine,str_list,parse):
        return [combine(base_url,parse(s))
                for s in str_list]
