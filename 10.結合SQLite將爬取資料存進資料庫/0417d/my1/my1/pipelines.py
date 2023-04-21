# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3


class My1Pipeline(object):
    def open_spider(self,spider):
        self.conn=sqlite3.connect('nba1.db')
        self.cur=self.conn.cursor()
        sql='''create table nbatable(
                title text,
                author text,
                date text)'''
        self.cur.execute(sql)        #只要有sql 就有 execute
        
    def close_spider(self,spider):    
        self.conn.commit()
        self.conn.close()
                
    
    def process_item(self, item, spider):
        title=item['title']
        author=item['author']
        date=item['date']
        x=(title,author,date)
        sql='''insert into nbatable values(?,?,?)'''
        self.conn.execute(sql,x)
        return item