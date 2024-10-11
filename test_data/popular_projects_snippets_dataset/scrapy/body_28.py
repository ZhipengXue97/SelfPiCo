# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/useragent.py
o = cls(crawler.settings["USER_AGENT"])
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
exit(o)
