# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from shuqing.items import ShuqingItem

class ShuSpider(CrawlSpider):
    name = 'shu'
    allowed_domains = ['www.szwj72.cn']
    # start_urls = ['http://www.szwj72.cn/t/shuqingsanwen/index.html']
    # start_urls = ['http://www.szwj72.cn/t/aiqingsanwen/index_29.html']
    # start_urls = ['http://www.szwj72.cn/aiqing/qinggan/index.html']
    start_urls = ['http://www.szwj72.cn/Article/aqzw/index_63.html']

    # 每一页的匹配规则
    # pagelink = LinkExtractor(allow=r'/t/shuqingsanwen/index_\d+.html')
    # pagelink = LinkExtractor(allow=r'/t/aiqingsanwen/index_\d+.html')
    # pagelink = LinkExtractor(allow=r'/aiqing/qinggan/index_\d+.html')
    pagelink = LinkExtractor(allow=r'http://www.szwj72.cn/Article/aqzw/index_\d+.html')
    # 每一页里的每个帖子的匹配规则
    # contentlink =       LinkExtractor(allow=r'http://www.szwj72.cn/Article/hsyy/\d+/\d+.html')
    # contentlink =       LinkExtractor(allow=r'http://www.szwj72.cn/Article/aqzw/\d+/\d+.html')
    # contentlink =       LinkExtractor(allow=r'http://www.szwj72.cn/aiqing/qinggan/\d+/\d+.html')
    contentlink =       LinkExtractor(allow=r'http://www.szwj72.cn/Article/aqzw/\d+/\d+.html')

    rules = (
        # Rule(pagelink,process_links = "deal_links"),
        Rule(contentlink, callback = 'parse_item'),
        Rule(pagelink),
    )

    # links 是当前response里提取出来的链接列表
    # def deal_links(self, links):
    #     for each in links:
    #         # each.url = each.url
    #         print each.url
    #     return links

    def parse_item(self, response):
        # print response.url
        item = ShuqingItem()
        # item['title'] = response.xpath('/html/body/div[1]/div/div[1]/div/header/h1/a/text()').extract()
        # # 添加时间
        # item['addtime'] = response.xpath('/html/body/div[1]/div/div[1]/div/header/h1/a/text()').extract()
        # item['cate'] = response.xpath('/html/body/div[1]/div/div[1]/div/header/div/span[2]/a/text()').extract()
        # # 内容
        # item['content'] = response.xpath('/html/body/div[1]/div/div[1]/div/article/p/text()').extract()
        item['title'] = response.xpath('/html/body/div[1]/div/div/div[1]/div[2]/h3/text()').extract()
        # 添加时间
        item['addtime'] = response.xpath('/html/body/div[1]/div/div/div[1]/h6/text()').extract()
        item['cate'] = response.xpath('/html/body/div[1]/div/div/div[1]/h6/a[1]/text()').extract()
        # 内容
        item['content'] = response.xpath('/html/body/div[1]/div/div/div[1]/div[4]/p/text()').extract()
        # 链接
        item['url'] = response.url

        yield item
        # print item
