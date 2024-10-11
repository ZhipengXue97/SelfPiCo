# Extracted from ./data/repos/scrapy/scrapy/exporters.py
if self._headers_not_written:
    self._headers_not_written = False
    self._write_headers_and_set_fields_to_export(item)

fields = self._get_serialized_fields(item, default_value="", include_empty=True)
values = list(self._build_row(x for _, x in fields))
self.csv_writer.writerow(values)
