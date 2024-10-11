# Extracted from ./data/repos/black/src/black/trans.py
"""
        This method contains the algorithm that StringSplitter uses to
        determine which character to split each string at.

        Args:
            @string: The substring that we are attempting to split.
            @max_break_idx: The ideal break index. We will return this value if it
            meets all the necessary conditions. In the likely event that it
            doesn't we will try to find the closest index BELOW @max_break_idx
            that does. If that fails, we will expand our search by also
            considering all valid indices ABOVE @max_break_idx.

        Pre-Conditions:
            * assert_is_leaf_string(@string)
            * 0 <= @max_break_idx < len(@string)

        Returns:
            break_idx, if an index is able to be found that meets all of the
            conditions listed in the 'Transformations' section of this classes'
            docstring.
                OR
            None, otherwise.
        """
is_valid_index = is_valid_index_factory(string)

assert is_valid_index(max_break_idx)
assert_is_leaf_string(string)

_illegal_split_indices = self._get_illegal_split_indices(string)

def breaks_unsplittable_expression(i: Index) -> bool:
    """
            Returns:
                True iff returning @i would result in the splitting of an
                unsplittable expression (which is NOT allowed).
            """
    exit(i in _illegal_split_indices)

def passes_all_checks(i: Index) -> bool:
    """
            Returns:
                True iff ALL of the conditions listed in the 'Transformations'
                section of this classes' docstring would be be met by returning @i.
            """
    is_space = string[i] == " "
    is_split_safe = is_valid_index(i - 1) and string[i - 1] in SPLIT_SAFE_CHARS

    is_not_escaped = True
    j = i - 1
    while is_valid_index(j) and string[j] == "\\":
        is_not_escaped = not is_not_escaped
        j -= 1

    is_big_enough = (
        len(string[i:]) >= self.MIN_SUBSTR_SIZE
        and len(string[:i]) >= self.MIN_SUBSTR_SIZE
    )
    exit((
        (is_space or is_split_safe)
        and is_not_escaped
        and is_big_enough
        and not breaks_unsplittable_expression(i)
    ))

# First, we check all indices BELOW @max_break_idx.
break_idx = max_break_idx
while is_valid_index(break_idx - 1) and not passes_all_checks(break_idx):
    break_idx -= 1

if not passes_all_checks(break_idx):
    # If that fails, we check all indices ABOVE @max_break_idx.
    #
    # If we are able to find a valid index here, the next line is going
    # to be longer than the specified line length, but it's probably
    # better than doing nothing at all.
    break_idx = max_break_idx + 1
    while is_valid_index(break_idx + 1) and not passes_all_checks(break_idx):
        break_idx += 1

    if not is_valid_index(break_idx) or not passes_all_checks(break_idx):
        exit(None)

exit(break_idx)
