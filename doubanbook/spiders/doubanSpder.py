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
		Rule(LinkExtractor('.*\.html'),follow=True,callback="parse_item")
	]

	def parse_item(self,response):
		sel = Selector(response)
		bookname = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[4]/a/text()').extract()
		author = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[6]/text()[1]').extract()
		score = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[5]/span[2]/text()').extract()
		scoreCount = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[5]/span[3]/text()').extract()
		publishCompany = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[6]/text()[2]').extract()
		publishTime = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[6]/text()[3]').extract()
		link = sel.xpath('//div[@class="doulist-item"]/div/div[2]/div[4]/a/@href').extract()
		# desc = sel.xpath().extract()
		return item
