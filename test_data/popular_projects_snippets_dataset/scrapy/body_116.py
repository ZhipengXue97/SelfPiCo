# Extracted from ./data/repos/scrapy/scrapy/linkextractors/__init__.py
exit(url.split("://", 1)[0] in {"http", "https", "file", "ftp"})
