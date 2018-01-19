# -*- coding: utf-8 -*-
# import scrapy
# from sun.items import SunItem
#
# class SunwzSpider(scrapy.Spider):
#     name = "sunwz"
#     allowed_domains = ["wz.sun0769.com"]
#     # start_urls = (
#     #     'http://www.wz.sun0769.com/',
#     # )
#     url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
#     offset = 0
#
#     start_urls = [url + str(offset)]
#
#     def parse(self, response):
#         # pass
#         # 链接
#         links = response.xpath("//div[@class='greyframe']/table//td/a[@class='news14']/@href").extract()
#
#         for link in links:
#             if self.offset <= 71130:
#                 self.offset += 30
#                 yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
#     # 处理每一个帖子
#     def parse_item(self, response):
#         item = SunItem()
#         # 标题
#         item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
#         # 编号
#         item['number'] = item['title'].split(' ')[-1].split(":")[-1]
#
#         # 文字内容，默认先取出有图片情况下的文字内容列表
#         content = response.xpath('//div[@class="contentext"]/text()').extract()
#
#
#         if len(content) == 0:
#             content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
#
#              # content为列表，通过join方法拼接为字符串，并去除首尾空格
#             item['content'] = "".join(content).strip()
#
#         else:
#             item['content'] = "".join(content).strip()
#
#
#         # 链接
#         item['url'] = response.url
#
#         yield item
#
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# from sun.items import SunItem
#
#
# class SunSpider(CrawlSpider):
#     name = 'sunwz'
#     allowed_domains = ['wz.sun0769.com']
#     start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']
#
#     rules = (
#         Rule(LinkExtractor(allow=r'type=4&page=\d+')),
#         Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback = 'parse_item'),
#     )
#
#     def parse_item(self, response):
#         item = SunItem()
#
#         #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
#         #i['name'] = response.xpath('//div[@id="name"]').extract()
#         #i['description'] = response.xpath('//div[@id="description"]').extract()
#         item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
# # 编号
#         item['number'] = item['title'].split(' ')[-1].split(":")[-1]
# # 内容
#         item['content'] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
# # 链接
#         item['url'] = response.url
#
#         yield item

# 导入核心机制scrapy
import scrapy
# 
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sun.items import SunItem


class DongdongSpider(CrawlSpider):
    name = 'sunwz'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 每一页的匹配规则
    pagelink = LinkExtractor(allow=("type=4"))
    # 每一页里的每个帖子的匹配规则
    contentlink = LinkExtractor(allow=(r"/html/question/\d+/\d+.shtml"))

    rules = (
        # 本案例的url被web服务器篡改，需要调用process_links来处理提取出来的url
        Rule(pagelink, process_links = "deal_links"),
        Rule(contentlink, callback = "parse_item")
    )

    # links 是当前response里提取出来的链接列表
    def deal_links(self, links):
        for each in links:
            each.url = each.url.replace("?","&").replace("Type&","Type?")
        return links

    def parse_item(self, response):
        item = SunItem()
        # 标题
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        # 编号
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]
        # 内容，先使用有图片情况下的匹配规则，如果有内容，返回所有内容的列表集合
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        # 如果没有内容，则返回空列表，则使用无图片情况下的匹配规则
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        # 链接
        item['url'] = response.url

        yield item
