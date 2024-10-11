# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
from twisted.internet import reactor

exit(isinstance(reactor, asyncioreactor.AsyncioSelectorReactor))
