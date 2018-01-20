# -*- coding: utf-8 -*-
import scrapy
# from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crm.items import CrmItem


class CrmartSpider(scrapy.Spider):
    name = 'crmart'
    allowed_domains = ['www.scwczx.cn']
    # offset = 528
    # url = "http://www.12ky.com/c/astro/list_949_"

    # end = ".html"
    # start_urls = (
    #     url+str(offset)+end,
    # )
    offset = 2658
    url = "http://www.scwczx.cn/newsInfo.aspx?pkId="
    start_urls = (
        url+str(offset),
    )
    # 每一页的匹配规则
    # pagelink = LinkExtractor(allow=(r"c/astro/list_\d+_\d+.html?WebShieldDRSessionVerify=Xmulfd0RRGuq7C5ZrMDt"))
    # page_lx = LinkExtractor(allow = ('list_949_\d+'))
    #
    # contentlink = LinkExtractor(allow=(r"c/astro/\d+.html"))
    #
    # rules = (
    #     Rule(pagelink, callback = "parse_item"),
    #     Rule(contentlink, callback = "parse_item")
    # )

    def parse(self, response):
        # print(response)
        item = CrmItem()
        # article = response.xpath("/html/body/div[1]/section")
        # article = ('//*[@id="_ctl1"]/table/tbody/tr/td/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table')


        # for each in article:
            # item['title'] = response.xpath('.//ul/li[1]/a[2]/text()').extract()[0]
            # item['img_url'] = response.xpath('.//ul/li[1]/a[1]/img/@src').extract()[0]
            # item['content'] = response.xpath('.//ul/li[1]/div[@class="intro"]/text()').extract()[0]
            # # 链接
            # item['url'] = response.url
        title= response.xpath('//*[@id="_ctl1"]/table/tbody/tr/td/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/h1/text()').extract()[0]

        # item['date'] = response.xpath('//*[@id="_ctl1"]/table/tbody/tr/td/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/p[3]/span[2]/text()').extract()[0]
        # item['number'] = response.xpath('//*[@id="_ctl1"]/table/tbody/tr/td/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/p[3]/span[3]/text()').extract()[0]
        item['content'] = response.xpath('//*[@id="n-content"]').extract()[0]
        # if len(content) == 0:
        #     content = response.xpath('//*[@id="n-content"]/p[2]/span/img/@src').extract()
        #     item['content'] = "".join(content).strip()
        # else:
        #     item['content'] = "".join(content).strip()
        # 链接
        item['url'] = response.url
        yield item

        # if(self.offset > 1):
            # self.offset -= 1
            # yield scrapy.Request(self.url + str(self.offset) + self.end, callback = self.parse)
        if(self.offset < 7080):
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
