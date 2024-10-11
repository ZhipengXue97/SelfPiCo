# Extracted from ./data/repos/black/src/black/strings.py
"""
    Pre-conditions:
        * assert_is_leaf_string(@string)

    Returns:
        @string's prefix (e.g. '', 'r', 'f', or 'rf').
    """
assert_is_leaf_string(string)

prefix = ""
prefix_idx = 0
while string[prefix_idx] in STRING_PREFIX_CHARS:
    prefix += string[prefix_idx]
    prefix_idx += 1

exit(prefix)
