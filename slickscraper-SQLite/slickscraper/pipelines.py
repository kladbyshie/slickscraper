# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import unicodedata
import re

#lib used to clean titles
rep_lib = {'&lpar;':'(',
            '&rpar;':')',
            '&colon;':':',
            '&period;':'.',
            '&plus;':'+',
            '&percnt;':'%',
            '&sol;':'/',
            '&dollar;':'$',
            '&comma;':','
            }

class SlickscraperPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('items.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS item_tb""")
        self.curr.execute("""CREATE TABLE item_tb(
                        date text,
                        item_title text,
                        item_price text,
                        item_oldprice text,
                        item_site text,
                        item_link text)""")

#cleaner cleans the output
    def cleaner(self,item):
        if item['item_link'][0] == "/":
            try:
                item['item_link'] = 'www.slickdeals.net' + item['item_link']
            except:
                pass
           
        for thing in item:
            try:
                item[thing] = item[thing].strip()
            except:
                pass

        for title in rep_lib.keys():                
            item['item_title'] = re.sub(title, rep_lib[title], item['item_title'])

    def process_item(self, item, spider):
        self.cleaner(item)
        self.store_db(item)
        return item

    def store_db(self, item):   
        self.curr.execute("""INSERT INTO item_tb VALUES (?, ?, ?, ?, ?, ?) IF NOT EXISTS""",(
            item['date'],
            item['item_title'],
            item['item_price'],
            item['item_oldprice'],
            item['item_site'],
            item['item_link'],
            ))
        self.conn.commit()

