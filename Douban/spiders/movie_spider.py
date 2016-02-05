from scrapy import Spider,Request
from Douban.items import DoubanItem
import re
import time
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

    def attr_xpath_pattern(self):
        with open(self.pattern_file_name) as f:
            for line in f:
                yield tuple(line.strip().split(' '))
                
    def parse(self,response):
        item = DoubanItem()

        for attr,xpath_pattern in self.attr_xpath_pattern():
            item[attr] = ','.join(response.xpath(xpath_pattern).extract()).encode('utf-8')

        yield item
            
        douban_urls = response.xpath(self.urls_pattern).extract()
        for url in douban_urls:
            yield Request(url,self.parse)
                
