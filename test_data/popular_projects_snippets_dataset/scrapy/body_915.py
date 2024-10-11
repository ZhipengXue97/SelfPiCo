# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
mintime = time() - age
for key, slot in list(self.slots.items()):
    if not slot.active and slot.lastseen + slot.delay < mintime:
        self.slots.pop(key).close()
