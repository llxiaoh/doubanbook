from scrapy.spiders import Rule,CrawlSpider
from scrapy.selector import Selector
import logging
from scrapy.linkextractors import LinkExtractor
from doubanbook.items import DoubanbookItem


class doubanSpider(CrawlSpider):
	name = "doubanSpider"
	#allowed_domians =["ttps://www.douban.com/doulist/1264675/"]
	start_urls=[
		"https://www.douban.com/doulist/1264675/",
	]
	rules = [
		Rule(LinkExtractor(''),follow=True,callback="parse_item")
	]

	def parse_item(self,response):
		sel = Selector(response)
		item = DoubanbookItem()
		bookname = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[4]/a/text()').extract()
		author = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[6]/text()[1]').extract()
		score = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[5]/span[2]/text()').extract()
		scoreCount = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[5]/span[3]/text()').extract()
		publishCompany = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[6]/text()[2]').extract()
		publishTime = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[6]/text()[3]').extract()
		link = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[4]/a/@href').extract()
		item['bookName'] = [b.encode("utf-8") for b in bookname]
		item['author'] = [a.encode("utf-8") for a in author]
		item['score'] = [s.encode("utf-8") for s in score]
		item['scoreCount'] = [sc.encode("utf-8") for sc in scoreCount]
		item['publishCompany'] = [p.encode('utf-8') for p in publishCompany]
		item['publishTime'] = [pt.encode('utf-8') for pt in publishTime]
		item['link'] = link

		# desc = sel.xpath().extract()
		return item
