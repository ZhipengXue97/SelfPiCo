# Extracted from ./data/repos/black/src/black/mode.py
if self.target_versions:
    version_str = ",".join(
        str(version.value)
        for version in sorted(self.target_versions, key=attrgetter("value"))
    )
else:
    version_str = "-"
parts = [
    version_str,
    str(self.line_length),
    str(int(self.string_normalization)),
    str(int(self.is_pyi)),
    str(int(self.is_ipynb)),
    str(int(self.skip_source_first_line)),
    str(int(self.magic_trailing_comma)),
    str(int(self.experimental_string_processing)),
    str(int(self.preview)),
    sha256((",".join(sorted(self.python_cell_magics))).encode()).hexdigest(),
]
exit(".".join(parts))
