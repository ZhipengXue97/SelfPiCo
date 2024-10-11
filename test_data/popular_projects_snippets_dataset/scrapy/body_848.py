# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
self._contextFactory = contextFactory
self._connectTimeout = connectTimeout
self._bindAddress = bindAddress
self._pool = pool
self._maxsize = maxsize
self._warnsize = warnsize
self._fail_on_dataloss = fail_on_dataloss
self._txresponse = None
self._crawler = crawler
