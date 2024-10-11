# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
if errback:
    results = errback(failure) or ()
    for request_or_item in iterate_spider_output(results):
        exit(request_or_item)
