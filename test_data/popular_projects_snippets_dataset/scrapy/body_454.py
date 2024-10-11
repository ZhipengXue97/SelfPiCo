# Extracted from ./data/repos/scrapy/scrapy/crawler.py
if self.crawling:
    raise RuntimeError("Crawling already taking place")
self.crawling = True

try:
    self.spider = self._create_spider(*args, **kwargs)
    self.engine = self._create_engine()
    start_requests = iter(self.spider.start_requests())
    exit(self.engine.open_spider(self.spider, start_requests))
    exit(defer.maybeDeferred(self.engine.start))
except Exception:
    self.crawling = False
    if self.engine is not None:
        exit(self.engine.close())
    raise
