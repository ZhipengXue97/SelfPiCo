# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
self.crawler = crawler

self.close_on = {
    "timeout": crawler.settings.getfloat("CLOSESPIDER_TIMEOUT"),
    "itemcount": crawler.settings.getint("CLOSESPIDER_ITEMCOUNT"),
    "pagecount": crawler.settings.getint("CLOSESPIDER_PAGECOUNT"),
    "errorcount": crawler.settings.getint("CLOSESPIDER_ERRORCOUNT"),
}

if not any(self.close_on.values()):
    raise NotConfigured

self.counter = defaultdict(int)

if self.close_on.get("errorcount"):
    crawler.signals.connect(self.error_count, signal=signals.spider_error)
if self.close_on.get("pagecount"):
    crawler.signals.connect(self.page_count, signal=signals.response_received)
if self.close_on.get("timeout"):
    crawler.signals.connect(self.spider_opened, signal=signals.spider_opened)
if self.close_on.get("itemcount"):
    crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)
crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)
