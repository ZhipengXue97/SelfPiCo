# Extracted from ./data/repos/scrapy/scrapy/crawler.py
"""
        Return a :class:`~scrapy.crawler.Crawler` object.

        * If ``crawler_or_spidercls`` is a Crawler, it is returned as-is.
        * If ``crawler_or_spidercls`` is a Spider subclass, a new Crawler
          is constructed for it.
        * If ``crawler_or_spidercls`` is a string, this function finds
          a spider with this name in a Scrapy project (using spider loader),
          then creates a Crawler instance for it.
        """
if isinstance(crawler_or_spidercls, Spider):
    raise ValueError(
        "The crawler_or_spidercls argument cannot be a spider object, "
        "it must be a spider class (or a Crawler object)"
    )
if isinstance(crawler_or_spidercls, Crawler):
    exit(crawler_or_spidercls)
exit(self._create_crawler(crawler_or_spidercls))
