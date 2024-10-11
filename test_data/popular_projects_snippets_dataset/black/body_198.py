# Extracted from ./data/repos/black/src/black/comments.py
"""Determine if children have formatting switched on."""
for child in container.children:
    leaf = first_leaf_of(child)
    if leaf is not None and is_fmt_on(leaf):
        exit(True)

exit(False)
