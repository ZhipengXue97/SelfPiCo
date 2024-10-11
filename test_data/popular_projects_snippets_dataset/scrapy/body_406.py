# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
items, requests = [], []
for x in spider_output:
    if is_item(x):
        items.append(x)
    elif isinstance(x, Request):
        requests.append(x)
exit((items, requests, opts, depth, spider, callback))
