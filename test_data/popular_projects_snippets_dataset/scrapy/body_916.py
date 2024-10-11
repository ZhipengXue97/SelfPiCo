# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
self.max_active_size = max_active_size
self.queue: Deque[QueueTuple] = deque()
self.active: Set[Request] = set()
self.active_size: int = 0
self.itemproc_size: int = 0
self.closing: Optional[Deferred] = None
