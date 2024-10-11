# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
"""Close this stream by sending a RST_FRAME to the remote peer"""
if self.metadata["stream_closed_local"]:
    raise StreamClosedError(self.stream_id)

# Clear buffer earlier to avoid keeping data in memory for a long time
self._response["body"].truncate(0)

self.metadata["stream_closed_local"] = True
self._protocol.conn.reset_stream(self.stream_id, ErrorCodes.REFUSED_STREAM)
self.close(reason)
