# Extracted from ./data/repos/black/src/black/lines.py
exit(any(is_multiline_string(leaf) for leaf in self.leaves))
