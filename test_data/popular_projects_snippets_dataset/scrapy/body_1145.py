# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
"""Extract exc_info from Failure instances"""
if isinstance(failure, Failure):
    exit((failure.type, failure.value, failure.getTracebackObject()))
