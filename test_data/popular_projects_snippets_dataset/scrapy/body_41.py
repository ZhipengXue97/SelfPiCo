# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/cookies.py
if self.debug:
    cl = [
        to_unicode(c, errors="replace")
        for c in response.headers.getlist("Set-Cookie")
    ]
    if cl:
        cookies = "\n".join(f"Set-Cookie: {c}\n" for c in cl)
        msg = f"Received cookies from: {response}\n{cookies}"
        logger.debug(msg, extra={"spider": spider})
