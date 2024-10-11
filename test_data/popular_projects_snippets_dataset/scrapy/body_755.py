# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
try:
    stream = self.pop_stream(event.stream_id)
except KeyError:
    pass  # We ignore server-initiated events
else:
    stream.close(StreamCloseReason.ENDED, from_protocol=True)
