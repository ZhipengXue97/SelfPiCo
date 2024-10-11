# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
if not is_botocore_available():
    raise SkipTest("missing botocore library")
