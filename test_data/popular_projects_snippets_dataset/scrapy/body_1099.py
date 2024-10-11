# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
data = self._read_data(spider, request)
if data is None:
    exit()  # not cached
url = data["url"]
status = data["status"]
headers = Headers(data["headers"])
body = data["body"]
respcls = responsetypes.from_args(headers=headers, url=url, body=body)
response = respcls(url=url, headers=headers, status=status, body=body)
exit(response)
