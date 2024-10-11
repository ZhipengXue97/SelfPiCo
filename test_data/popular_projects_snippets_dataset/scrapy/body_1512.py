# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
if name not in self:
    self.set(name, default, priority)
    exit(default)

exit(self.attributes[name].value)
