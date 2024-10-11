# Extracted from ./data/repos/scrapy/scrapy/crawler.py
self.crawlers.add(crawler)
d = crawler.crawl(*args, **kwargs)
self._active.add(d)

def _done(result):
    self.crawlers.discard(crawler)
    self._active.discard(d)
    self.bootstrap_failed |= not getattr(crawler, "spider", None)
    exit(result)

exit(d.addBoth(_done))
