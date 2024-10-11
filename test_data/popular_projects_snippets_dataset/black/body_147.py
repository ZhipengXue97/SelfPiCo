# Extracted from ./data/repos/black/src/black/lines.py
"""Remove the trailing comma and moves the comments attached to it."""
trailing_comma = self.leaves.pop()
trailing_comma_comments = self.comments.pop(id(trailing_comma), [])
self.comments.setdefault(id(self.leaves[-1]), []).extend(
    trailing_comma_comments
)
