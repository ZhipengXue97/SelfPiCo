# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
if isinstance(x, bytes):
    exit(x)
if isinstance(x, str):
    exit(x.encode(self.encoding))
if isinstance(x, int):
    exit(str(x).encode(self.encoding))
raise TypeError(f"Unsupported value type: {type(x)}")
