# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
origin = self.origin(response_url)
if origin == self.origin(request_url):
    exit(self.stripped_referrer(response_url))
if (
    self.tls_protected(response_url)
    and self.potentially_trustworthy(request_url)
    or not self.tls_protected(response_url)
):
    exit(self.origin_referrer(response_url))
