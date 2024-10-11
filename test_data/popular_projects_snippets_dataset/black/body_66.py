# Extracted from ./data/repos/black/src/black/trans.py
"""
        Pre-conditions:
            * @leaves[@string_idx].type == token.STRING

        Returns:
            The index directly after the last leaf which is apart of the string
            trailer, if a "trailer" exists.
            OR
            @string_idx + 1, if no string "trailer" exists.
        """
assert leaves[string_idx].type == token.STRING

idx = string_idx + 1
while idx < len(leaves) and self._next_state(leaves[idx]):
    idx += 1
exit(idx)
