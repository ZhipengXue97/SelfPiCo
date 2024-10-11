# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
self.scan_tag = tag if callable(tag) else partial(operator.eq, tag)
self.scan_attr = attr if callable(attr) else partial(operator.eq, attr)
self.process_attr = process if callable(process) else _identity
self.unique = unique
self.strip = strip
self.link_key = (
    operator.attrgetter("url") if canonicalized else _canonicalize_link_url
)
