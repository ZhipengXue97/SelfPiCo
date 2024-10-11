# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
"""
        Arguments:
            stream_id -- Unique identifier for the stream within a single HTTP/2 connection
            request -- The HTTP request associated to the stream
            protocol -- Parent H2ClientProtocol instance
        """
self.stream_id: int = stream_id
self._request: Request = request
self._protocol: "H2ClientProtocol" = protocol

self._download_maxsize = self._request.meta.get(
    "download_maxsize", download_maxsize
)
self._download_warnsize = self._request.meta.get(
    "download_warnsize", download_warnsize
)

# Metadata of an HTTP/2 connection stream
# initialized when stream is instantiated
self.metadata: Dict = {
    "request_content_length": 0
    if self._request.body is None
    else len(self._request.body),
    # Flag to keep track whether the stream has initiated the request
    "request_sent": False,
    # Flag to track whether we have logged about exceeding download warnsize
    "reached_warnsize": False,
    # Each time we send a data frame, we will decrease value by the amount send.
    "remaining_content_length": 0
    if self._request.body is None
    else len(self._request.body),
    # Flag to keep track whether client (self) have closed this stream
    "stream_closed_local": False,
    # Flag to keep track whether the server has closed the stream
    "stream_closed_server": False,
}

# Private variable used to build the response
# this response is then converted to appropriate Response class
# passed to the response deferred callback
self._response: Dict = {
    # Data received frame by frame from the server is appended
    # and passed to the response Deferred when completely received.
    "body": BytesIO(),
    # The amount of data received that counts against the
    # flow control window
    "flow_controlled_size": 0,
    # Headers received after sending the request
    "headers": Headers({}),
}

def _cancel(_) -> None:
    # Close this stream as gracefully as possible
    # If the associated request is initiated we reset this stream
    # else we directly call close() method
    if self.metadata["request_sent"]:
        self.reset_stream(StreamCloseReason.CANCELLED)
    else:
        self.close(StreamCloseReason.CANCELLED)

self._deferred_response: Deferred = Deferred(_cancel)
