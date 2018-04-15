# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HakeItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    tag  = scrapy.Field()
    view = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
