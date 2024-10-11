# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
if self.DOWNLOAD_SLOT in request.meta:
    exit(cast(str, request.meta[self.DOWNLOAD_SLOT]))

key = urlparse_cached(request).hostname or ""
if self.ip_concurrency:
    key = dnscache.get(key, key)

exit(key)
