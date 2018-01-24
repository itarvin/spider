# -*- coding: utf-8 -*-
import scrapy
from movielists.items import MovielistsItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["80s.tw"]
    # start_urls = (
    #     'http://www.80s.tw/',
    # )
    start = 1
    url = "https://www.80s.tw/movie/list/-----p"
    start_urls = [url +str(start)]
    yuming = "https://www.80s.tw"


    def parse(self, response):
        # pass
        for i in range(0,25):
            links = response.xpath("//*[@id='block3']/div[3]/ul[2]/li["+str(i)+"]/a/@href").extract()
            for link in links:
                yield scrapy.Request(self.yuming + link, callback = self.parse_item)
        # 设置页码终止条件，并且每次发送新的页面请求调用parse方法处理
        if self.start <= 421:
            self.start += 1
            yield scrapy.Request(self.url + str(self.start), callback = self.parse)

    # 处理每个页面里
    def parse_item(self, response):
        item = MovielistsItem()
        # 标题
        item['title'] = response.xpath('//*[@id="minfo"]/div[2]/h1/text()').extract()
        # 别名
        aliastitle = response.xpath('//*[@id="minfo"]/div[2]/span[4]/text()').extract()
        item['aliastitle'] = "".join(aliastitle).strip()
        #演员
        item['actor'] = response.xpath('//*[@id="minfo"]/div[2]/span[5]/text()').extract()
        # 上映时间
        item['show'] = response.xpath('//*[@id="minfo"]/div[2]/div[1]/span[5]/text()').extract()
        # 简介
        brief=  response.xpath('//*[@id="movie_content"]/text()').extract()
        item['brief'] = "".join(brief).strip()
        # 豆瓣评分
        item['grade'] = response.xpath('//*[@id="minfo"]/div[2]/div[2]/span[1]/text()').extract()
        # 语言
        item['lang'] = response.xpath('//*[@id="minfo"]/div[2]/div[1]/span[3]/a/text()').extract()
        # 类型
        item['types'] = response.xpath('//*[@id="minfo"]/div[2]/div[1]/span[1]/a/text()').extract()
        # 视频截图
        item['image_url'] = response.xpath('//*[@id="minfo"]/div[1]/img/@src').extract()
        # 导演
        item['direct'] = response.xpath('//*[@id="minfo"]/div[2]/div[1]/span[4]/a/text()').extract()
        # 地区
        item['area'] = response.xpath('//*[@id="minfo"]/div[2]/div[1]/span[2]/text()').extract()
        # 链接
        item['url'] = response.url

        yield item
