# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/',
    )

    def parse(self, response):
        pass
