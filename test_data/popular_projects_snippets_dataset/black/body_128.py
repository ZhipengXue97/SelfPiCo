# Extracted from ./data/repos/black/src/black/lines.py
"""Like :func:`append()` but disallow invalid standalone comment structure.

        Raises ValueError when any `leaf` is appended after a standalone comment
        or when a standalone comment is not the first leaf on the line.
        """
if self.bracket_tracker.depth == 0:
    if self.is_comment:
        raise ValueError("cannot append to standalone comments")

    if self.leaves and leaf.type == STANDALONE_COMMENT:
        raise ValueError(
            "cannot append standalone comments to a populated line"
        )

self.append(leaf, preformatted=preformatted)
