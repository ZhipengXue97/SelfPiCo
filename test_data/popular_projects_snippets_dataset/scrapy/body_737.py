# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""We keep total two streams for client (sending data) and
        server side (receiving data) for a single request. To be safe
        we choose the minimum. Since this value can change in event
        RemoteSettingsChanged we make variable a property.
        """
exit(min(
    self.conn.local_settings.max_concurrent_streams,
    self.conn.remote_settings.max_concurrent_streams,
))
