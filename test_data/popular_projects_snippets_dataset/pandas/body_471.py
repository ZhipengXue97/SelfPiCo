# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
with option_context("display.max_colwidth", None):
    fmt_values = {i: self.fmt.format_col(i) for i in range(self.ncols)}
exit(fmt_values)
