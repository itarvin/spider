# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from TencentSpider.items import TencentItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    # pageLink = LinkExtractor(allow=("start=\d+"))
    pagelink = LinkExtractor(allow=("start=\d+"))
    # newlink = LinkExtractor(allow=("start=\d+"))
    rules = [
        Rule(pagelink,callback = "parseTencent",follow = True)
    ]
    def parseTencent(self,response):
    # def parse_item(self, response):
    #     i = TencentspiderItem()
    #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     #i['description'] = response.xpath('//div[@id="description"]').extract()
    #     return i
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = TencentItem()

            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            # item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] =  each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
