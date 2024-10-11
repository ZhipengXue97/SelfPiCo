# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
super().__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
self._proxyConf = proxyConf
self._contextFactory = contextFactory
