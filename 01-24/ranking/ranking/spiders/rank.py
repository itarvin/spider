# -*- coding: utf-8 -*-
import scrapy
from ranking.items import RankingItem

class RankSpider(scrapy.Spider):
    name = "rank"
    # allowed_domains = ["80s.tw"]
    # start_urls = (
    #     'http://www.80s.tw/',
    # )

    # def parse(self, response):
    #     pass
    # name = "moive"
    allowed_domains = ["80s.tw"]


    start = 1
    url = "https://www.80s.tw/movie/list/-----p"
    start_urls = [url +str(start)]
    yuming = "https://www.80s.tw"

    def parse(self, response):
        # 设置页码终止条件，并且每次发送新的页面请求调用parse方法处理
        item = RankingItem()
        for i in range(0,25):
            title = response.xpath("//*[@id='block3']/div[3]/ul[2]/li["+ str(i) +"]/h3/a/text()").extract()
            item['title'] = "".join(title).strip()
            movie_urls = response.xpath("//*[@id='block3']/div[3]/ul[2]/li["+ str(i) +"]/a/@href").extract()
            item['movie_url'] = (self.yuming + str(movie_urls))
            score = response.xpath("//*[@id='block3']/div[3]/ul[2]/li["+ str(i) +"]/a/span[2]/text()").extract()
            if len(score) == 0:
                item['score'] = "6.0"
            else:
                item['score'] = "".join(score).strip()
            tip = response.xpath("//*[@id='block3']/div[3]/ul[2]/li["+ str(i) +"]/span/text()").extract()
            if len(tip) == 0:
                item['tip'] = "itarvin"
            else:
                item['tip'] = "".join(tip).strip()
            item['image_url'] = response.xpath("//*[@id='block3']/div[3]/ul[2]/li["+ str(i) +"]/a/img/@src").extract()
            # item['res_url'] = response.url
            yield item
        if self.start <= 421:
            self.start += 1
            yield scrapy.Request(self.url + str(self.start), callback = self.parse)
