# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
if isinstance(tag, str):
    if tag[0] == "{" and tag[1 : len(XHTML_NAMESPACE) + 1] == XHTML_NAMESPACE:
        exit(tag.split("}")[-1])
exit(tag)
