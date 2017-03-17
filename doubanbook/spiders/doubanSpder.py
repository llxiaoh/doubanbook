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
		divs = sel.xpath('//div[@class="doulist-item"]/div[@class="mod"]/div[1]')
		for div in divs:
			link = div.xpath('./div[4]/a/@href')
			if len(link)>0:
				item = DoubanbookItem()
				t_link = link[0]
				bookname = div.xpath('./div[4]/a/text()').extract()
				author = div.xpath('./div[6]/text()[1]').extract()
				score = div.xpath('./div[5]/span[2]/text()').extract()
				scoreCount = div.xpath('./div[5]/span[3]/text()').extract()
				publishCompany = div.xpath('./div[6]/text()[2]').extract()
				publishTime = div.xpath('./div[6]/text()[3]').extract()
				item['bookName'] = [b.encode("utf-8") for b in bookname]
				item['author'] = [a.encode("utf-8") for a in author]
				item['score'] = [s.encode("utf-8") for s in score]
				item['scoreCount'] = [sc.encode("utf-8") for sc in scoreCount]
				item['publishCompany'] = [p.encode('utf-8') for p in publishCompany]
				item['publishTime'] = [pt.encode('utf-8') for pt in publishTime]
				item['link'] = t_link
				yield scrapy.Request(t_link,callback=self.parse_detail,meta={"item":item})

	def parse_detail(self,response):
		desc = response.xpath('//div[@id="link-report"]/text()').extract()
		item = response.meta["item"]
		item['desc'] = [d.encode("utf-8") for d in "".join(desc).lstrip().rstrip()]
		return item

