# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/httperror.py
if 200 <= response.status < 300:  # common case
    exit()
meta = response.meta
if meta.get("handle_httpstatus_all", False):
    exit()
if "handle_httpstatus_list" in meta:
    allowed_statuses = meta["handle_httpstatus_list"]
elif self.handle_httpstatus_all:
    exit()
else:
    allowed_statuses = getattr(
        spider, "handle_httpstatus_list", self.handle_httpstatus_list
    )
if response.status in allowed_statuses:
    exit()
raise HttpError(response, "Ignoring non-200 response")
