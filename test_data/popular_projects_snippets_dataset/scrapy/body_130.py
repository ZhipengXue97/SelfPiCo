# Extracted from ./data/repos/scrapy/scrapy/exporters.py
if self.first_item:
    self.first_item = False
else:
    self.file.write(b",")
    self._beautify_newline()
itemdict = dict(self._get_serialized_fields(item))
data = self.encoder.encode(itemdict)
self.file.write(to_bytes(data, self.encoding))
