# Extracted from ./data/repos/scrapy/scrapy/utils/response.py
"""Open the given response in a local web browser, populating the <base>
    tag for external links to work
    """
from scrapy.http import HtmlResponse, TextResponse

# XXX: this implementation is a bit dirty and could be improved
body = response.body
if isinstance(response, HtmlResponse):
    if b"<base" not in body:
        repl = rf'\1<base href="{response.url}">'
        body = re.sub(b"<!--.*?-->", b"", body, flags=re.DOTALL)
        body = re.sub(rb"(<head(?:>|\s.*?>))", to_bytes(repl), body)
    ext = ".html"
elif isinstance(response, TextResponse):
    ext = ".txt"
else:
    raise TypeError("Unsupported response type: " f"{response.__class__.__name__}")
fd, fname = tempfile.mkstemp(ext)
os.write(fd, body)
os.close(fd)
exit(_openfunc(f"file://{fname}"))
