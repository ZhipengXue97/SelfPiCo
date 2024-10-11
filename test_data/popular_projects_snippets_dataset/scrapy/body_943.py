# Extracted from ./data/repos/scrapy/scrapy/spiderloader.py
"""
        Return the Spider class for the given spider name. If the spider
        name is not found, raise a KeyError.
        """
try:
    exit(self._spiders[spider_name])
except KeyError:
    raise KeyError(f"Spider not found: {spider_name}")
