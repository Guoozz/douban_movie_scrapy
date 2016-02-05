from scrapy import Spider,Request
from Douban.items import DoubanItem
import re
import time
from scrapy.exceptions import IgnoreRequest

class MovieSpider(Spider):
    name='douban_movie'
    allowed_domains = ['douban.com']
    start_urls=[
        "http://movie.douban.com/subject/11589036/",
        "http://movie.douban.com/subject/25954475",
        'http://movie.douban.com/subject/6786002',
    ]
    
    def parse(self,response):
        item = DoubanItem()

        with open('douban_movie.txt') as f:
            for line in f:
                (attr,xpath_pattern) = tuple(line.strip().split(' '))
                item[attr] = ','.join(response.xpath(xpath_pattern).extract()).encode('utf-8')
                
            yield item
            
        with open('douban_movie_urls_pattern.txt') as f:
            douban_urls = response.xpath(f.read().strip()).extract()
                      
            for url in douban_urls:
                try:
                    yield Request(url,self.parse)
                except IgnoreRequest:
                    time.sleep(20)
                    yield Request(url,self.parse)
