# -*- coding: utf-8 -*-
import scrapy
from qxt.items import QxtItem


class QxtgoodsSpider(scrapy.Spider):
    name = "qxtgoods"
    allowed_domains = ["www.qixingtang.com"]
    offset = 2230
    url = "http://www.qixingtang.com/goods.php?id="
    start_urls = (
        url+str(offset),
    )

    def parse(self, response):

        item = QxtItem()

        item['goods_name'] = response.xpath('//div[@class="proname"]/text()').extract()

        item['art_no'] = response.xpath('//div[@class="promod"]/text()').extract()

        item['goods_brand'] = response.xpath('//div[@class="proband"]/text()').extract()

        item['goods_price'] = response.xpath('//*[@id="ECS_SHOPPRICE"]/text()').extract()

        item['img_url'] = response.xpath('//*[@id="PicBox"]/img/@src').extract()

        item['url'] = response.url

        yield item

        if(self.offset < 2408):
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
        # pass
