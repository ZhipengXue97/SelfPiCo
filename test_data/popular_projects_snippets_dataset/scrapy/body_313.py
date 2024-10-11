# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
for prefix, uri in self.namespaces:
    selector.register_namespace(prefix, uri)
