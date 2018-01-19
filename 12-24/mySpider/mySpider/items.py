# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from mySpider.items import ItcastItem


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # pass
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()
    
	def parse(self, response):
	    #open("teacher.html","wb").write(response.body).close()

	    # 存放老师信息的集合
	    #items = []

	    for each in response.xpath("//div[@class='li_txt']"):
	        # 将我们得到的数据封装到一个 `ItcastItem` 对象
	        item = ItcastItem()
	        #extract()方法返回的都是unicode字符串
	        name = each.xpath("h3/text()").extract()
	        title = each.xpath("h4/text()").extract()
	        info = each.xpath("p/text()").extract()

	        #xpath返回的是包含一个元素的列表
	        item['name'] = name[0]
	        item['title'] = title[0]
	        item['info'] = info[0]

	        #items.append(item)

	        #将获取的数据交给pipelines
	        yield item

	    # 返回数据，不经过pipeline
	    #return items