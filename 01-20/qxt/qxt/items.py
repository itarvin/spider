# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QxtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    goods_name = scrapy.Field()
    art_no = scrapy.Field()
    goods_brand = scrapy.Field()
    goods_price = scrapy.Field()
    img_url = scrapy.Field()
    url = scrapy.Field()
