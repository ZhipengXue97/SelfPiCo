# Extracted from ./data/repos/scrapy/scrapy/extensions/throttle.py
key = request.meta.get("download_slot")
exit((key, self.crawler.engine.downloader.slots.get(key)))
