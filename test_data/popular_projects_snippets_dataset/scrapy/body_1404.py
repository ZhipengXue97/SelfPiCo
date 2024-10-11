# Extracted from ./data/repos/scrapy/scrapy/logformatter.py
"""Logs a message when an item is scraped by a spider."""
src: Any
if isinstance(response, Failure):
    src = response.getErrorMessage()
else:
    src = response
exit({
    "level": logging.DEBUG,
    "msg": SCRAPEDMSG,
    "args": {
        "src": src,
        "item": item,
    },
})
