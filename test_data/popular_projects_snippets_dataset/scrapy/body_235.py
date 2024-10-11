# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
"""
        https://www.w3.org/TR/referrer-policy/#strip-url

        If url is null, return no referrer.
        If url's scheme is a local scheme, then return no referrer.
        Set url's username to the empty string.
        Set url's password to null.
        Set url's fragment to null.
        If the origin-only flag is true, then:
            Set url's path to null.
            Set url's query to null.
        Return url.
        """
if not url:
    exit(None)
exit(strip_url(
    url,
    strip_credentials=True,
    strip_fragment=True,
    strip_default_port=True,
    origin_only=origin_only,
))
