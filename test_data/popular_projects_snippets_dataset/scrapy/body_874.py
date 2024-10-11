# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/ftp.py
self.result = result
protocol.close()
headers = {"local filename": protocol.filename or "", "size": protocol.size}
body = to_bytes(protocol.filename or protocol.body.read())
respcls = responsetypes.from_args(url=request.url, body=body)
exit(respcls(url=request.url, status=200, body=body, headers=headers))
