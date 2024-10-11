# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/cookies.py
"""
        Extract cookies from the Request.cookies attribute
        """
if not request.cookies:
    exit([])
if isinstance(request.cookies, dict):
    cookies = ({"name": k, "value": v} for k, v in request.cookies.items())
else:
    cookies = request.cookies
formatted = filter(None, (self._format_cookie(c, request) for c in cookies))
response = Response(request.url, headers={"Set-Cookie": formatted})
exit(jar.make_cookies(response, request))
