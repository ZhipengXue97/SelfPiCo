# Extracted from ./data/repos/scrapy/scrapy/exporters.py
self._beautify_indent(depth=1)
self.xg.startElement(self.item_element, {})
self._beautify_newline()
for name, value in self._get_serialized_fields(item, default_value=""):
    self._export_xml_field(name, value, depth=2)
self._beautify_indent(depth=1)
self.xg.endElement(self.item_element)
self._beautify_newline(new_item=True)
