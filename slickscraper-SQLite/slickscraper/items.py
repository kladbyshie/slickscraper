# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SlickscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_title = scrapy.Field()
    item_price = scrapy.Field()
    item_oldprice = scrapy.Field()
    item_site = scrapy.Field()
    item_link = scrapy.Field()
    date = scrapy.Field()