# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
if self.dqs is None:
    exit(False)
try:
    self.dqs.push(request)
except ValueError as e:  # non serializable request
    if self.logunser:
        msg = (
            "Unable to serialize request: %(request)s - reason:"
            " %(reason)s - no more unserializable requests will be"
            " logged (stats being collected)"
        )
        logger.warning(
            msg,
            {"request": request, "reason": e},
            exc_info=True,
            extra={"spider": self.spider},
        )
        self.logunser = False
    assert self.stats is not None
    self.stats.inc_value("scheduler/unserializable", spider=self.spider)
    exit(False)
else:
    exit(True)
