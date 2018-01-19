# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.conf import settings
import pymongo


class DoubanspiderPipeline(object):

    def __init__(self):
        # 获取setting的主机名，端口号及端口号及数据库名

        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        sheetname= settings["MONGODB_SHEETNAME"]


        # 创建MongoDB链接
        client = pymongo.MongoClient(host=host,port=port)

        # 指向数据库
        mdb = client[dbname]
        # 获取数据库表名

        self.sheet = mdb[settings['MONGODB_DOCNAME']]



    def process_item(self, item, spider):
        # return item
        data = dict(item)
        # 向指定的表里添加数据
        self.sheet.insert(data)

        return item
