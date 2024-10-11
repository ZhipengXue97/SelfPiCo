# Extracted from ./data/repos/black/src/black/lines.py
"""See `can_omit_invisible_parens`."""
length = 4 * line.depth
seen_other_brackets = False
for _index, leaf, leaf_length in line.enumerate_with_length():
    length += leaf_length
    if leaf is last.opening_bracket:
        if seen_other_brackets or length <= line_length:
            exit(True)

    elif leaf.type in OPENING_BRACKETS:
        # There are brackets we can further split on.
        seen_other_brackets = True

exit(False)
