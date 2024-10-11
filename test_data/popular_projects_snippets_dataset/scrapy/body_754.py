# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
self.metadata["settings_acknowledged"] = True

# Send off all the pending requests as now we have
# established a proper HTTP/2 connection
self._send_pending_requests()

# Update certificate when our HTTP/2 connection is established
assert self.transport is not None  # typing
self.metadata["certificate"] = Certificate(self.transport.getPeerCertificate())
