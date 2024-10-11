# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/defaultheaders.py
for k, v in self._headers:
    request.headers.setdefault(k, v)
