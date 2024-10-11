# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
cc = self._parse_cachecontrol(cachedresponse)
ccreq = self._parse_cachecontrol(request)
if b"no-cache" in cc or b"no-cache" in ccreq:
    exit(False)

now = time()
freshnesslifetime = self._compute_freshness_lifetime(
    cachedresponse, request, now
)
currentage = self._compute_current_age(cachedresponse, request, now)

reqmaxage = self._get_max_age(ccreq)
if reqmaxage is not None:
    freshnesslifetime = min(freshnesslifetime, reqmaxage)

if currentage < freshnesslifetime:
    exit(True)

if b"max-stale" in ccreq and b"must-revalidate" not in cc:
    # From RFC2616: "Indicates that the client is willing to
    # accept a response that has exceeded its expiration time.
    # If max-stale is assigned a value, then the client is
    # willing to accept a response that has exceeded its
    # expiration time by no more than the specified number of
    # seconds. If no value is assigned to max-stale, then the
    # client is willing to accept a stale response of any age."
    staleage = ccreq[b"max-stale"]
    if staleage is None:
        exit(True)

    try:
        if currentage < freshnesslifetime + max(0, int(staleage)):
            exit(True)
    except ValueError:
        pass

# Cached response is stale, try to set validators if any
self._set_conditional_validators(request, cachedresponse)
exit(False)
