# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
# class MeiwenPipeline(object):
    # def process_item(self, item, spider):
    #     return item
import pymysql
####注意一定要导入配置，因为数据库的一些连接信息写在settings文件里的
#此类是把信息写入文档，写入时末尾都加了一个逗号，是为了数据的观看与直观性
#也方便以后用mysql语言直接导入数据
from scrapy.conf import settings
#下面是将爬取到的信息插入到MySQL数据库中
class MeiwenPipeline(object):
    def process_item(self, item, spider):
        host = settings['MYSQL_HOSTS']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c=settings['CHARSET']
        port=settings['MYSQL_PORT']
        title = json.dumps(item['title'], ensure_ascii = False)
        contents = json.dumps(item['content'], ensure_ascii = False)
        content1 = ''
        content2 = contents.strip()
        content  = content1.join(content2)
        addtime = json.dumps(item['addtime'], ensure_ascii = False)
        author = json.dumps(item['author'], ensure_ascii = False)
        #数据库连接
        con=pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
        #数据库游标
        cue=con.cursor()
        print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        try:
            cue.execute("insert into meiwen (title,addtime,author,hits,content,url) values(%s,%s,%s,%s,%s,%s)",[ title,addtime,author,item['hits'],content,item['url']])
            print("insert success")#测试语句
        except Exception as e:
            print('Insert error:',e)
            con.rollback()
        else:
            con.commit()
        con.close()
        return item
