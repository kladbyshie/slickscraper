# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
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
            '&comma;':',',
            '&excl;':'!'
            }

class SlickscraperPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = psycopg2.connect("host='localhost' dbname='Slickscraper' user='postgres' password='postgres'")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS item_tb(
                        date VARCHAR(255),
                        item_title VARCHAR(255) UNIQUE,
                        item_price VARCHAR(255),
                        item_oldprice VARCHAR(255),
                        item_site VARCHAR(255),
                        item_link VARCHAR(255) UNIQUE)""")

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
        self.curr.execute("""INSERT INTO item_tb VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (item_link) DO NOTHING""", (
            item['date'],
            item['item_title'],
            item['item_price'],
            item['item_oldprice'],
            item['item_site'],
            item['item_link'],
            ))
        self.conn.commit()

