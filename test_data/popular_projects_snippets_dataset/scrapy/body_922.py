# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
self.slot: Optional[Slot] = None
self.spidermw: SpiderMiddlewareManager = SpiderMiddlewareManager.from_crawler(
    crawler
)
itemproc_cls: Type[ItemPipelineManager] = load_object(
    crawler.settings["ITEM_PROCESSOR"]
)
self.itemproc: ItemPipelineManager = itemproc_cls.from_crawler(crawler)
self.concurrent_items: int = crawler.settings.getint("CONCURRENT_ITEMS")
self.crawler: Crawler = crawler
self.signals: SignalManager = crawler.signals
self.logformatter: LogFormatter = crawler.logformatter
