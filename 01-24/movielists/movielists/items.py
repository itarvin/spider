# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovielistsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    aliastitle = scrapy.Field()
    actor = scrapy.Field()
    show = scrapy.Field()
    brief = scrapy.Field()
    grade = scrapy.Field()
    lang = scrapy.Field()
    types = scrapy.Field()
    image_url = scrapy.Field()
    direct = scrapy.Field()
    area = scrapy.Field()
    url = scrapy.Field()
