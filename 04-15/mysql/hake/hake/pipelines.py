# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class HakePipeline(object):
#     def process_item(self, item, spider):
#         return item
# import codecs
import json
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

# from scrapy.conf import settings
# import pymongo
#
# class HakePipeline(object):
#     def __init__(self):
#         # 获取setting主机名、端口号和数据库名
#         host = settings['MONGODB_HOST']
#         port = settings['MONGODB_PORT']
#         dbname = settings['MONGODB_DBNAME']
#
#         # pymongo.MongoClient(host, port) 创建MongoDB链接
#         client = pymongo.MongoClient(host=host,port=port)
#
#         # 指向指定的数据库
#         mdb = client[dbname]
#         # 获取数据库里存放数据的表名
#         self.post = mdb[settings['MONGODB_DOCNAME']]
#
#
#     def process_item(self, item, spider):
#         data = dict(item)
#         # 向指定的表里添加数据
#         self.post.insert(data)
#         return item



# MySQl 存储
import pymysql
####注意一定要导入配置，因为数据库的一些连接信息写在settings文件里的
#此类是把信息写入文档，写入时末尾都加了一个逗号，是为了数据的观看与直观性
#也方便以后用mysql语言直接导入数据
from scrapy.conf import settings
#下面是将爬取到的信息插入到MySQL数据库中
class HakePipeline(object):
     def process_item(self, item, spider):
        host = settings['MYSQL_HOSTS']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c=settings['CHARSET']
        port=settings['MYSQL_PORT']
        content = json.dumps(item['content'], ensure_ascii = False)
#数据库连接
        con=pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
#数据库游标
        cue=con.cursor()
        print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        #sql="insert into gamerank (rank,g_name,g_type,g_status,g_hot) values(%s,%s,%s,%s,%s)" % (item['rank'],item['game'],item['type'],item['status'],item['hot'])
        try:
            # cue.execute("insert into hakeinfo (title,url,times,tag,view,content) values(%s,%s,%s,%s,%s,%s)",[ item['title'],item['url'],item['time'],item['tag'],item['view'],item['content']])
            cue.execute("insert into hakeinfo (title,url,times,tag,view,content) values(%s,%s,%s,%s,%s,%s)",[ item['title'],item['url'],item['time'],item['tag'],item['view'],content])
            print("insert success")#测试语句
        except Exception as e:
            print('Insert error:',e)
            con.rollback()
        else:
            con.commit()
        con.close()
        return item
