# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
"""Normalize values to bytes"""
if value is None:
    value = []
elif isinstance(value, (str, bytes)):
    value = [value]
elif not hasattr(value, "__iter__"):
    value = [value]

exit([self._tobytes(x) for x in value])
