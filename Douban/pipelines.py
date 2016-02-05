# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

class DoubanPipeline(object):

    def __init__(self):
        self.file = open('douban_movie.json','w')
        self.exporter = JsonLinesItemExporter(self.file,ensure_ascii=False,indent=4,
                                              encoding='utf-8',sort_keys=True)
        
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def spider_closed(self,spider):
        self.file.close()
        
