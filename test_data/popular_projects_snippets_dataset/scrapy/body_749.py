# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""Called by Twisted when the transport connection is lost.
        No need to write anything to transport here.
        """
# Cancel the timeout if not done yet
self.setTimeout(None)

# Notify the connection pool instance such that no new requests are
# sent over current connection
if not reason.check(connectionDone):
    self._conn_lost_errors.append(reason)

self._conn_lost_deferred.callback(self._conn_lost_errors)

for stream in self.streams.values():
    if stream.metadata["request_sent"]:
        close_reason = StreamCloseReason.CONNECTION_LOST
    else:
        close_reason = StreamCloseReason.INACTIVE
    stream.close(close_reason, self._conn_lost_errors, from_protocol=True)

self.metadata["active_streams"] -= len(self.streams)
self.streams.clear()
self._pending_request_stream_pool.clear()
self.conn.close_connection()
