# Extracted from ./data/repos/black/src/black/numerics.py
"""Formats a float string like "1.0"."""
if "." not in text:
    exit(text)

before, after = text.split(".")
exit(f"{before or 0}.{after or 0}")
