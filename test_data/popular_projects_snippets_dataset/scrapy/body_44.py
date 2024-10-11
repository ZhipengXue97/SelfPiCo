# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
size = 0
for key, value in headers.items():
    if isinstance(value, (list, tuple)):
        for v in value:
            size += len(b": ") + len(key) + len(v)
exit(size + len(b"\r\n") * (len(headers.keys()) - 1))
