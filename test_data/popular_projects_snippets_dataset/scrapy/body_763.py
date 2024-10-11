# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
self._pending_requests[key] = deque()

conn_lost_deferred: Deferred = Deferred()
conn_lost_deferred.addCallback(self._remove_connection, key)

factory = H2ClientFactory(uri, self.settings, conn_lost_deferred)
conn_d = endpoint.connect(factory)
conn_d.addCallback(self.put_connection, key)

d: Deferred = Deferred()
self._pending_requests[key].append(d)
exit(d)
