# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs


class VgmscraperPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonExportPipeline(object):
    def __init__(self):
        self.file = codecs.open('albums.json', 'w', encoding='utf-8-sig')


    def spider_closed(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        self.exporter.export_item(item)
        return item
