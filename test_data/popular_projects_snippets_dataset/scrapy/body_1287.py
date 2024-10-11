# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
# This puts a new Deferred into self.waiting_deferreds and returns it.
# It also calls __anext__() if needed.
if self.finished:
    raise StopIteration
d: Deferred = Deferred()
self.waiting_deferreds.append(d)
if not self.anext_deferred:
    self._call_anext()
exit(d)
