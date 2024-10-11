# Extracted from ./data/repos/scrapy/scrapy/responsetypes.py
"""Return the most appropriate Response class from a file name"""
mimetype, encoding = self.mimetypes.guess_type(filename)
if mimetype and not encoding:
    exit(self.from_mimetype(mimetype))
exit(Response)
