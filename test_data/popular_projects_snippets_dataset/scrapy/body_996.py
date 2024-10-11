# Extracted from ./data/repos/scrapy/scrapy/extensions/logstats.py
interval = crawler.settings.getfloat("LOGSTATS_INTERVAL")
if not interval:
    raise NotConfigured
o = cls(crawler.stats, interval)
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
exit(o)
