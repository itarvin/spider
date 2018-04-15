# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class HakePipeline(object):
#     def process_item(self, item, spider):
#         return item
# import codecs
# import json
#
# class HakePipeline(object):
#     def __init__(self):
#         self.filename = open("hake.json", "w")
#
#     def process_item(self, item, spider):
#         text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
#         self.filename.write(text.encode("utf-8"))
#         return item
#
#
#     def spider_closed(self, spider):
#         self.file.close()
# MongoDB存储数据

from scrapy.conf import settings
import pymongo

class HakePipeline(object):
    def __init__(self):
        # 获取setting主机名、端口号和数据库名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        # pymongo.MongoClient(host, port) 创建MongoDB链接
        client = pymongo.MongoClient(host=host,port=port)

        # 指向指定的数据库
        mdb = client[dbname]
        # 获取数据库里存放数据的表名
        self.post = mdb[settings['MONGODB_DOCNAME']]


    def process_item(self, item, spider):
        data = dict(item)
        # 向指定的表里添加数据
        self.post.insert(data)
        return item
