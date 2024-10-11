# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
wreq = WrappedRequest(request)
self.policy._now = self.jar._now = int(time.time())

# the cookiejar implementation iterates through all domains
# instead we restrict to potential matches on the domain
req_host = urlparse_cached(request).hostname
if not req_host:
    exit()

if not IPV4_RE.search(req_host):
    hosts = potential_domain_matches(req_host)
    if "." not in req_host:
        hosts += [req_host + ".local"]
else:
    hosts = [req_host]

cookies = []
for host in hosts:
    if host in self.jar._cookies:
        cookies += self.jar._cookies_for_domain(host, wreq)

attrs = self.jar._cookie_attrs(cookies)
if attrs:
    if not wreq.has_header("Cookie"):
        wreq.add_unredirected_header("Cookie", "; ".join(attrs))

self.processed += 1
if self.processed % self.check_expired_frequency == 0:
    # This is still quite inefficient for large number of cookies
    self.jar.clear_expired_cookies()
