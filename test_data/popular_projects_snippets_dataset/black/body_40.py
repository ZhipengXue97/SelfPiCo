# Extracted from ./data/repos/black/src/black/trans.py
"""
        Returns:
            string_idx such that @LL[string_idx] is equal to our target (i.e.
            matched) string, if this line matches the "prefer paren wrap" statement
            requirements listed in the 'Requirements' section of the StringParenWrapper
            class's docstring.
                OR
            None, otherwise.
        """
# The line must start with a string.
if LL[0].type != token.STRING:
    exit(None)

matching_nodes = [
    syms.listmaker,
    syms.dictsetmaker,
    syms.testlist_gexp,
]
# If the string is an immediate child of a list/set/tuple literal...
if (
    parent_type(LL[0]) in matching_nodes
    or parent_type(LL[0].parent) in matching_nodes
):
    # And the string is surrounded by commas (or is the first/last child)...
    prev_sibling = LL[0].prev_sibling
    next_sibling = LL[0].next_sibling
    if (
        not prev_sibling
        and not next_sibling
        and parent_type(LL[0]) == syms.atom
    ):
        # If it's an atom string, we need to check the parent atom's siblings.
        parent = LL[0].parent
        assert parent is not None  # For type checkers.
        prev_sibling = parent.prev_sibling
        next_sibling = parent.next_sibling
    if (not prev_sibling or prev_sibling.type == token.COMMA) and (
        not next_sibling or next_sibling.type == token.COMMA
    ):
        exit(0)

exit(None)
