# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
code = color_string.lstrip("#")
if self._is_shorthand_color(color_string):
    exit((code[0] * 2 + code[1] * 2 + code[2] * 2).upper())
else:
    exit(code.upper())
