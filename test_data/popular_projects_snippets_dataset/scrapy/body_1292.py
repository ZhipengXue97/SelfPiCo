# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
"""Wraps an iterable calling an errback if an error is caught while
    iterating it.
    """
it = iter(iterable)
while True:
    try:
        exit(next(it))
    except StopIteration:
        break
    except Exception:
        errback(failure.Failure(), *a, **kw)
