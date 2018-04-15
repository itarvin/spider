# -*- coding: utf-8 -*-
import scrapy
import re
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider,Rule
from hake.items import HakeItem

class HakesSpider(scrapy.Spider):
    # 如果遇到网页状态为404,500
    handle_httpstatus_list = [404, 500]
    name = 'hakes'
    allowed_domains = ['weixianmanbu.com']
    urls = 'http://www.weixianmanbu.com/article/'
    offset = 3
    end = '.html'
    start_urls = [
        urls + str(offset) + end
    ]
    # 每一页的匹配规则
    # pagelink = LinkExtractor(allow=(r"/page_\d+.html/"))
    # # 每一页里的每个帖子的匹配规则
    # contentlink = LinkExtractor(allow=(r"urls/article/\d+.html/"))
    # rules = (
    #     # 本案例的url被web服务器篡改，需要调用process_links来处理提取出来的url
    #     Rule(pagelink, process_links = "deal_links"),
    #     Rule(contentlink, callback = "parse_item")
    # )


    # links 是当前response里提取出来的链接列表
    # def deal_links(self, links):
        # return links
        # print links
    def parse(self, response):
        if response.status in self.handle_httpstatus_list:
            self.offset += 2
            yield scrapy.Request(self.urls + str(self.offset) + self.end, callback = self.parse)
        else:
            item = HakeItem()
            # 标题
            item['title'] = response.xpath('/html/body/div[2]/div[1]/div/div[1]/header/h1/text()').extract()
            item['time'] = response.xpath('/html/body/div[2]/div[1]/div/div[1]/header/div/span[1]/text()').extract()

            item['view'] = response.xpath('/html/body/div[2]/div[1]/div/div[1]/header/div/span[3]/text()').extract()
            # view = ''
            # for s in views:
            #     if s.is_number():
            #         view += s
            # item['view'] = view
            item['tag'] = response.xpath('/html/body/div[2]/div[1]/div/div[1]/header/div/span[2]/a/text()').extract()
            item['content'] = response.xpath('/html/body/div[2]/div[1]/div/div[1]/article/p/text()').extract()
            # item['content'] = re.sub(r'\s+','', content)
            # 链接
            item['url'] = response.url
            yield item
            # print item

            self.offset += 1
            yield scrapy.Request(self.urls + str(self.offset) + self.end, callback = self.parse)
