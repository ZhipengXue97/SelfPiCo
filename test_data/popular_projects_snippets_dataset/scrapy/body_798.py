# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
if self.factory.method.upper() == b"HEAD":
    self.factory.page(b"")
elif self.length is not None and self.length > 0:
    self.factory.noPage(self._connection_lost_reason)
else:
    self.factory.page(response)
self.transport.loseConnection()
