# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class JobPipeline(object):
    def __init__(self):
        self.filename = open("job.json", "w")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.filename.write(text.encode("utf-8"))
        return item


    def spider_closed(self, spider):
        self.file.close()
