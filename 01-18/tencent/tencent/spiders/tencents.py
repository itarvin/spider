# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem

from tencent.items import TencentItem


class TencentsSpider(CrawlSpider):
    name = 'tencents'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    page_lx = LinkExtractor(allow = ('start=\d+'))

    rules = [
        #提取匹配,并使用spider的parse方法进行分析;并跟进链接(没有callback意味着follow默认为True)
        Rule(page_lx, callback = 'parseContent', follow = True)
    ]

    # def parse_item(self, response):
        # i = TencentItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

    def parseContent(self, response):
        for each in response.xpath('//*[@class="even"]'):
            name = each.xpath('./td[1]/a/text()').extract()[0]
            detailLink = each.xpath('./td[1]/a/@href').extract()[0]
            positionInfo = each.xpath('./td[2]/text()').extract()[0]

            peopleNumber = each.xpath('./td[3]/text()').extract()[0]
            workLocation = each.xpath('./td[4]/text()').extract()[0]
            publishTime = each.xpath('./td[5]/text()').extract()[0]
            #print name, detailLink, catalog,recruitNumber,workLocation,publishTime

            item = TencentItem()
            item['name']=name.encode('utf-8')
            item['detailLink']=detailLink.encode('utf-8')
            item['positionInfo']=positionInfo.encode('utf-8')
            item['peopleNumber']=peopleNumber.encode('utf-8')
            item['workLocation']=workLocation.encode('utf-8')
            item['publishTime']=publishTime.encode('utf-8')

            yield item
