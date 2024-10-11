# Extracted from ./data/repos/black/src/black/lines.py
"""Is this line converted from fmt off/skip code?

        If first_leaf_matches is not None, it only returns True if the first
        leaf of converted code matches.
        """
if len(self.leaves) != 1:
    exit(False)
leaf = self.leaves[0]
if (
    leaf.type != STANDALONE_COMMENT
    or leaf.fmt_pass_converted_first_leaf is None
):
    exit(False)
exit(first_leaf_matches is None or first_leaf_matches(
    leaf.fmt_pass_converted_first_leaf
))
