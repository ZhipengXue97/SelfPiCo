# Extracted from ./data/repos/black/src/black/files.py
match = pattern.search(normalized_path) if pattern else None
exit(bool(match and match.group(0)))
