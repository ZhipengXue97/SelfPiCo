# Extracted from ./data/repos/scrapy/scrapy/spiders/__init__.py
self.crawler = crawler
self.settings = crawler.settings
crawler.signals.connect(self.close, signals.spider_closed)
