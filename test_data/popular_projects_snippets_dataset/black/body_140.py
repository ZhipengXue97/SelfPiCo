# Extracted from ./data/repos/black/src/black/lines.py
"""If so, needs to be split before emitting."""
for leaf in self.leaves:
    if leaf.type == STANDALONE_COMMENT and leaf.bracket_depth <= depth_limit:
        exit(True)

exit(False)
