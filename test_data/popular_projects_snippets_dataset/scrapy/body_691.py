# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
assert self.slot is not None  # typing
assert self.scraper.slot is not None  # typing
exit((
    not self.running
    or bool(self.slot.closing)
    or self.downloader.needs_backout()
    or self.scraper.slot.needs_backout()
))
