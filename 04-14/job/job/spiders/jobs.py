# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from job.items import JobItem

class JobsSpider(CrawlSpider):
    name = "jobs"
    allowed_domains = ["web.jobbole.com"]
    start_urls = (
        'http://web.jobbole.com/category/javascript-2/page/2/',
        'http://web.jobbole.com/category/html5/page/2/',
        'http://web.jobbole.com/category/css/page/2/',
        'http://web.jobbole.com/category/basic-tech/page/2/',
        'http://web.jobbole.com/all-posts/page/2/'
    )
    # 每一页的匹配规则
    pagelink = LinkExtractor(allow=(r"/page/\d+/"))
    # 每一页里的每个帖子的匹配规则
    contentlink = LinkExtractor(allow=(r"/\d+/"))
    rules = (
        # 本案例的url被web服务器篡改，需要调用process_links来处理提取出来的url
        Rule(pagelink, process_links = "deal_links"),
        Rule(contentlink, callback = "parse_item")
    )

    # links 是当前response里提取出来的链接列表
    def deal_links(self, links):
        return links
    def parse_item(self, response):
        item = JobItem()
        # 标题
        item['title'] = response.xpath('/html/head/title/text()').extract()
        addtime = response.xpath('//*[@id="wrapper"]/div[3]/div[1]/div[2]/p/text()').extract()
        item['addtime'] = "".join(addtime).strip()
        # 内容，先使用有图片情况下的匹配规则，如果有内容，返回所有内容的列表集合
        content = response.xpath('//*[@id="wrapper"]/div[3]/div[1]/div[3]/p/text()').extract()
        # 如果没有内容，则返回空列表，则使用无图片情况下的匹配规则
        if len(content) == 0:
            content = response.xpath('//*[@id="wrapper"]/div[3]/div[1]/div[3]/p[1]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        # 链接
        item['url'] = response.url
        yield item
