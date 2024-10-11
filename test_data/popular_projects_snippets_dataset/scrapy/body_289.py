# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
if callable(method):
    exit(method)
if isinstance(method, str):
    exit(getattr(spider, method, None))
