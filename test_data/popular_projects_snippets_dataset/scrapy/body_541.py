# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
self._body = b""  # used by encoding detection
if isinstance(body, str):
    if self._encoding is None:
        raise TypeError(
            "Cannot convert unicode body - "
            f"{type(self).__name__} has no encoding"
        )
    self._body = body.encode(self._encoding)
else:
    super()._set_body(body)
