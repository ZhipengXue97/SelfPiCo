# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
try:
    exit(self.request.cb_kwargs)
except AttributeError:
    raise AttributeError(
        "Response.cb_kwargs not available, this response "
        "is not tied to any request"
    )
