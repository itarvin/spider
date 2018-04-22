# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeiwenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    addtime = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    hits = scrapy.Field()
    url = scrapy.Field()
