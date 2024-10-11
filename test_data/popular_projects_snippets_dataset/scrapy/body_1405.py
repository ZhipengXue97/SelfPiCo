# Extracted from ./data/repos/scrapy/scrapy/logformatter.py
"""Logs a message when an item is dropped while it is passing through the item pipeline."""
exit({
    "level": logging.WARNING,
    "msg": DROPPEDMSG,
    "args": {
        "exception": exception,
        "item": item,
    },
})
