# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
# check redirected request to patch "Referer" header if necessary
redirected_urls = request.meta.get("redirect_urls", [])
if redirected_urls:
    request_referrer = request.headers.get("Referer")
    # we don't patch the referrer value if there is none
    if request_referrer is not None:
        # the request's referrer header value acts as a surrogate
        # for the parent response URL
        #
        # Note: if the 3xx response contained a Referrer-Policy header,
        #       the information is not available using this hook
        parent_url = safe_url_string(request_referrer)
        policy_referrer = self.policy(parent_url, request).referrer(
            parent_url, request.url
        )
        if policy_referrer != request_referrer:
            if policy_referrer is None:
                request.headers.pop("Referer")
            else:
                request.headers["Referer"] = policy_referrer
