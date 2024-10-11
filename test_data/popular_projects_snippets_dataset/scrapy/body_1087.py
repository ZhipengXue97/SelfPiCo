# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
if r not in self._cc_parsed:
    cch = r.headers.get(b"Cache-Control", b"")
    parsed = parse_cachecontrol(cch)
    if isinstance(r, Response):
        for key in self.ignore_response_cache_controls:
            parsed.pop(key, None)
    self._cc_parsed[r] = parsed
exit(self._cc_parsed[r])
