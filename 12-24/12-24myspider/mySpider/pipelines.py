# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json

class ItcastPipeline(object):
    # __init__ 可选，初始化
    def __init__(self):
        # 创建文件
        self.filename = open("teacher.json", "w")
    #处理item数据 ，必选
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii = False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))
        return item
    # 可选 ,结束时调用
    def close_spider(self,spider):
        self.filename.close()
