from scrapy import cmdline
cmdline.execute("scrapy crawl dbbook -o items.json -t json".split())