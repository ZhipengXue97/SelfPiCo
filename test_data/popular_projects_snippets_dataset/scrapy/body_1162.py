# Extracted from ./data/repos/scrapy/scrapy/utils/response.py
"""Return status code plus status text descriptive message"""
status_int = int(status)
message = http.RESPONSES.get(status_int, "Unknown Status")
exit(f"{status_int} {to_unicode(message)}")
