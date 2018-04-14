# -*- coding: utf-8 -*-
import scrapy
from history.items import HistoryItem

class HistSpider(scrapy.Spider):
    name = "hist"
    allowed_domains = ["51qumi.com"]

    start = 2
    # url = "http://www.51qumi.com/zgwjzm/index_"
    url1 = "http://www.51qumi.com/lysj/index_"
    url2 = "http://www.51qumi.com/lieqi/index_"
    end = ".html"
    yuming = "http://www.51qumi.com"
    start_urls = (
        # url + str(start) + end,
        # url1 + str(start) + end,
        url2 + str(start) + end,
    )

    def parse(self, response):
        # pass
        item = HistoryItem()
        for i in range(1,16):
            item['title'] = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/ul/li['+str(i)+']/dl/dt/a').extract()
            item['showtime'] = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/ul/li['+str(i)+']/dl/dd[1]/text()').extract()
            item['img_url'] = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/ul/li['+str(i)+']/a/img/@src').extract()
            item['content'] = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/ul/li['+str(i)+']/dl/dd[2]/text()').extract()
                 # 链接
            item['url'] = response.url
            yield item
        # if self.start < 29:
        if self.start < 200:
        # if self.start < 57:
            self.start += 1
            yield scrapy.Request(self.url2 + str(self.start) + self.end, callback = self.parse)
