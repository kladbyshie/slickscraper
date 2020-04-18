# -*- coding: utf-8 -*-
import scrapy
from ..items import SlickscraperItem
from datetime import date

class SlickdealsSpider(scrapy.Spider):
    name = 'slickdeals'
    allowed_domains = ['slickdeals.net']
    start_urls = ['http://www.slickdeals.net/']

    def parse(self, response):
        items=SlickscraperItem()
        
        all_items = response.css('div.fpItem')
        today=date.today()
        for item in all_items:
            item_title = item.css('.itemTitle::text').get()
            item_price = item.css('.itemPrice::text').get()
            item_oldprice = item.css('.oldListPrice::text').get()
            item_site = item.css('.itemStore::text').get()
            item_link = item.css('a.itemTitle::attr(href)').get()
            
            items['item_title'] = item_title
            items['item_price'] = item_price
            items['item_oldprice'] = item_oldprice
            items['item_site'] = item_site
            items['item_link'] = item_link
            items['date'] = today

            yield items
 
