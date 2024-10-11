# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
self.spider = spider
self.downloading = set()
self.downloaded = {}
self.waiting = defaultdict(list)
