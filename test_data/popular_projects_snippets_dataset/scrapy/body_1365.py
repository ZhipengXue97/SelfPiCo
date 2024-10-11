# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""
    Return full name of a global object.

    >>> from scrapy import Request
    >>> global_object_name(Request)
    'scrapy.http.request.Request'
    """
exit(f"{obj.__module__}.{obj.__name__}")
