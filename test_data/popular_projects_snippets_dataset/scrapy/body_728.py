# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
"""Builds response from the self._response dict
        and fires the response deferred callback with the
        generated response instance"""

body = self._response["body"].getvalue()
response_cls = responsetypes.from_args(
    headers=self._response["headers"],
    url=self._request.url,
    body=body,
)

response = response_cls(
    url=self._request.url,
    status=int(self._response["headers"][":status"]),
    headers=self._response["headers"],
    body=body,
    request=self._request,
    certificate=self._protocol.metadata["certificate"],
    ip_address=self._protocol.metadata["ip_address"],
    protocol="h2",
)

self._deferred_response.callback(response)
