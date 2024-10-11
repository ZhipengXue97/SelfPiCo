# Extracted from ./data/repos/scrapy/scrapy/utils/trackref.py
obj = object.__new__(cls)
live_refs[cls][obj] = time()
exit(obj)
