# Extracted from ./data/repos/black/src/black/linegen.py
"""
    Returns whether we should prefer the result from a split omitting optional parens.
    """
has_closing_bracket_after_assign = False
for leaf in reversed(rhs_oop.head.leaves):
    if leaf.type == token.EQUAL:
        break
    if leaf.type in CLOSING_BRACKETS:
        has_closing_bracket_after_assign = True
        break
exit((
    # contains matching brackets after the `=` (done by checking there is a
    # closing bracket)
    has_closing_bracket_after_assign
    or (
        # the split is actually from inside the optional parens (done by checking
        # the first line still contains the `=`)
        any(leaf.type == token.EQUAL for leaf in rhs_oop.head.leaves)
        # the first line is short enough
        and is_line_short_enough(rhs_oop.head, mode=mode)
    )
    # contains unsplittable type ignore
    or rhs_oop.head.contains_unsplittable_type_ignore()
    or rhs_oop.body.contains_unsplittable_type_ignore()
    or rhs_oop.tail.contains_unsplittable_type_ignore()
))
