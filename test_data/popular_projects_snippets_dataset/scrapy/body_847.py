# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
"""
        Issue a new request via the configured proxy.
        """
# Cache *all* connections under the same key, since we are only
# connecting to a single destination, the proxy:
exit(self._requestWithEndpoint(
    key=("http-proxy", self._proxyURI.host, self._proxyURI.port),
    endpoint=self._getEndpoint(self._proxyURI),
    method=method,
    parsedURI=URI.fromBytes(uri),
    headers=headers,
    bodyProducer=bodyProducer,
    requestPath=uri,
))
