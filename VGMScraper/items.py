# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlbumItem(scrapy.Item):
    name = scrapy.Field()
    artist = scrapy.Field()
    date = scrapy.Field()
    tracks = scrapy.Field()
