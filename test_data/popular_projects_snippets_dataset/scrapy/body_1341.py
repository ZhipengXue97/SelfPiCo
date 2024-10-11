# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
"""Get Scrapy config file as a ConfigParser"""
sources = get_sources(use_closest)
cfg = ConfigParser()
cfg.read(sources)
exit(cfg)
