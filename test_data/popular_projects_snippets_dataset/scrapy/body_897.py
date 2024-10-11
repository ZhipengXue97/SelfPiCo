# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
if self.randomize_delay:
    exit(random.uniform(0.5 * self.delay, 1.5 * self.delay))
exit(self.delay)
