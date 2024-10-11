# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
max_items, max_requests = 0, 0
if self.items:
    max_items = max(self.items)
if self.requests:
    max_requests = max(self.requests)
exit(max(max_items, max_requests))
