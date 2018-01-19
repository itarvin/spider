# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 电影标题
    title = scrapy.Field()
    # 电影评分
    star = scrapy.Field()
    # 电影信息
    bd = scrapy.Field()
    # 简介
    quote = scrapy.Field()
