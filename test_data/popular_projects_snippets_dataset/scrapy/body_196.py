# Extracted from ./data/repos/scrapy/scrapy/responsetypes.py
"""Try to guess the appropriate response based on the body content.
        This method is a bit magic and could be improved in the future, but
        it's not meant to be used except for special cases where response types
        cannot be guess using more straightforward methods."""
chunk = body[:5000]
chunk = to_bytes(chunk)
if not binary_is_text(chunk):
    exit(self.from_mimetype("application/octet-stream"))
lowercase_chunk = chunk.lower()
if b"<html>" in lowercase_chunk:
    exit(self.from_mimetype("text/html"))
if b"<?xml" in lowercase_chunk:
    exit(self.from_mimetype("text/xml"))
if b"<!doctype html>" in lowercase_chunk:
    exit(self.from_mimetype("text/html"))
exit(self.from_mimetype("text"))
