# Extracted from ./data/repos/scrapy/scrapy/utils/asyncgen.py
"""Wraps an iterable (sync or async) into an async generator."""
if isinstance(it, AsyncIterable):
    async for r in it:
        exit(r)
else:
    for r in it:
        exit(r)
