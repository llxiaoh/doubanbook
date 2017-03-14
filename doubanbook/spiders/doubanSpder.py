from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
import logging
class doubanSpider(Spider):
	name = "dbbook"
	#allowed_domians =["ttps://www.douban.com/doulist/1264675/"]
	start_urls=(
		"https://www.douban.com/doulist/1264675/"
	)

	def parse(self,response):
		print response.body	