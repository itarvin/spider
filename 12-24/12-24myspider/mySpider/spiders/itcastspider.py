# -*- coding: utf-8 -*-

import scrapy
from mySpider.items import ItcastItem
# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许爬虫的范围
    allowed_domains = ["http://www.itcast.cn/"]
    # 爬虫请求的url
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#aandroid",
        "http://www.itcast.cn/channel/teacher.shtml#ac",
        "http://www.itcast.cn/channel/teacher.shtml#acloud",
        "http://www.itcast.cn/channel/teacher.shtml#aios",
        "http://www.itcast.cn/channel/teacher.shtml#ajavaee",
        "http://www.itcast.cn/channel/teacher.shtml#anetmarket",
        "http://www.itcast.cn/channel/teacher.shtml#aphp",
        "http://www.itcast.cn/channel/teacher.shtml#apython",
        "http://www.itcast.cn/channel/teacher.shtml#astack",
        "http://www.itcast.cn/channel/teacher.shtml#aui",
        "http://www.itcast.cn/channel/teacher.shtml#aweb"
    ]

    def parse(self,response):
        # 下载网页源码
        # with open("teacher.html", "w") as f:
        #     f.write(response.body)
        # 通过scrapy自带xpath获取里面的节点
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # teacherItem = []
        #遍历节点集合,
        for each in teacher_list:
            # 实例化对象用来保存数据
            item = ItcastItem()
            # 名字 ,extract()转unicode字符串
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()

            # item['name'] = name[0].encode('gbk')
            # item['title'] = title[0].encode('gbk')
            # item['info'] = info[0].encode('gbk')
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            yield item
            # teacherItem.append(item)
            # print name[0]
            # print title[0]
            # print info[0]
        # return teacherItem
