# Extracted from ./data/repos/black/src/black/trans.py
"""
        Returns:
            string_idx such that @LL[string_idx] is equal to our target (i.e.
            matched) string, if this line matches the ternary expression
            requirements listed in the 'Requirements' section of this classes'
            docstring.
                OR
            None, otherwise.
        """
# If this line is apart of a ternary expression and the first leaf
# contains the "else" keyword...
if (
    parent_type(LL[0]) == syms.test
    and LL[0].type == token.NAME
    and LL[0].value == "else"
):
    is_valid_index = is_valid_index_factory(LL)

    idx = 2 if is_valid_index(1) and is_empty_par(LL[1]) else 1
    # The next visible leaf MUST contain a string...
    if is_valid_index(idx) and LL[idx].type == token.STRING:
        exit(idx)

exit(None)
