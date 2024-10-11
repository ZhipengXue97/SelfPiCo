# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
self.value = value
if isinstance(self.value, BaseSettings):
    self.priority = max(self.value.maxpriority(), priority)
else:
    self.priority = priority
