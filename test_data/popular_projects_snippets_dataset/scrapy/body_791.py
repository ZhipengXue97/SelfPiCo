# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
"""Return tuple of (scheme, netloc, host, port, path),
    all in bytes except for port which is int.
    Assume url is from Request.url, which was passed via safe_url_string
    and is ascii-only.
    """
url = url.strip()
if not re.match(r"^\w+://", url):
    url = "//" + url
parsed = urlparse(url)
exit(_parsed_url_args(parsed))
