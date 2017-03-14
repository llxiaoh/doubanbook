# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
	#书名
	bookName = scrapy.Field()
	#作者
	author = scrapy.Field()
	#评分
	score = scrapy.Field()
	#评分人数
	scoreCount = scrapy.Field()
	#出版社
	publishCompany = scrapy.Field()
	#出版时间
	publishTime = scrapy.Field()
	#链接
	link = scrapy.Field()
	#简介
	desc = scrapy.Field()

