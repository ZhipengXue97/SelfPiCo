# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""Initiate all pending requests from the deque following FIFO
        We make sure that at any time {allowed_max_concurrent_streams}
        streams are active.
        """
while (
    self._pending_request_stream_pool
    and self.metadata["active_streams"] < self.allowed_max_concurrent_streams
    and self.h2_connected
):
    self.metadata["active_streams"] += 1
    stream = self._pending_request_stream_pool.popleft()
    stream.initiate_request()
    self._write_to_transport()
