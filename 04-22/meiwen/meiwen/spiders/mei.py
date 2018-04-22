# -*- coding: utf-8 -*-
import scrapy
import time
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider,Rule
from meiwen.items import MeiwenItem

class MeiSpider(scrapy.Spider):
    # 如果遇到网页状态为404,500
    handle_httpstatus_list = [404, 500]
    name = 'mei'
    allowed_domains = ['www.jj59.com']
    url = 'https://www.jj59.com/qingganwenzhang/0'
    offset = 320
    end = ".html"
    start_urls = [
        url + str(offset) + end
    ]

    # def parse(self, response):
        # pass
        # 每一页的匹配规则
    # pagelink = LinkExtractor(allow=(r"/list_39_\d+/"))
    # 每一页里的每个帖子的匹配规则
    # contentlink = LinkExtractor(allow=(r"/qingganwenzhang/\d+.html/"))
    # rules = (
    #     # 本案例的url被web服务器篡改，需要调用process_links来处理提取出来的url
    #     # Rule(pagelink, process_links = "deal_links"),
    #     Rule(contentlink, callback = "parse_item")
    # )

    # links 是当前response里提取出来的链接列表
    # def deal_links(self, links):
    #     return links
    def parse(self, response):
        if response.status in self.handle_httpstatus_list:
            self.offset += 2
            yield scrapy.Request(self.url + str(self.offset) + self.end, callback = self.parse)
        else:
            item = MeiwenItem()
            # 标题
            title = response.xpath('/html/head/title/text()').extract()
            if len(title) == 0:
                item['title'] = "itarvin"
            else :
                item['title'] = title
            addtime = response.xpath('/html/body/span/div[2]/div[1]/div[1]/div[3]/text()').extract()
            if len(addtime) == 0:
                item['addtime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            else :
                item['addtime'] = addtime
            item['hits'] = response.xpath('//*[@id="dj"]/text()').extract()
            # 内容，先使用有图片情况下的匹配规则，如果有内容，返回所有内容的列表集合
            content = response.xpath('/html/body/div[2]/div[1]/div[1]/div[4]/p[2]/text()').extract()
            if len(content) == 0:
                item['content'] = "itarvin"
            else :
                item['content'] = content
            # 链接
            author = response.xpath('/html/body/span/div[2]/div[1]/div[1]/div[3]/a/text()')
            if len(author) == 0:
                item['author'] = "itarvin"
            else :
                item['author'] = author
            item['url'] = response.url
            yield item
            # print item

            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset) + self.end, callback = self.parse)
