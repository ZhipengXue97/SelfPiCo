# Extracted from ./data/repos/black/src/black/trans.py
LL = line.leaves
assert len(string_indices) == 1, (
    f"{self.__class__.__name__} should only find one match at a time, found"
    f" {len(string_indices)}"
)
string_idx = string_indices[0]

QUOTE = LL[string_idx].value[-1]

is_valid_index = is_valid_index_factory(LL)
insert_str_child = insert_str_child_factory(LL[string_idx])

prefix = get_string_prefix(LL[string_idx].value).lower()

# We MAY choose to drop the 'f' prefix from substrings that don't
# contain any f-expressions, but ONLY if the original f-string
# contains at least one f-expression. Otherwise, we will alter the AST
# of the program.
drop_pointless_f_prefix = ("f" in prefix) and fstring_contains_expr(
    LL[string_idx].value
)

first_string_line = True

string_op_leaves = self._get_string_operator_leaves(LL)
string_op_leaves_length = (
    sum(len(str(prefix_leaf)) for prefix_leaf in string_op_leaves) + 1
    if string_op_leaves
    else 0
)

def maybe_append_string_operators(new_line: Line) -> None:
    """
            Side Effects:
                If @line starts with a string operator and this is the first
                line we are constructing, this function appends the string
                operator to @new_line and replaces the old string operator leaf
                in the node structure. Otherwise this function does nothing.
            """
    maybe_prefix_leaves = string_op_leaves if first_string_line else []
    for i, prefix_leaf in enumerate(maybe_prefix_leaves):
        replace_child(LL[i], prefix_leaf)
        new_line.append(prefix_leaf)

ends_with_comma = (
    is_valid_index(string_idx + 1) and LL[string_idx + 1].type == token.COMMA
)

def max_last_string_column() -> int:
    """
            Returns:
                The max allowed width of the string value used for the last
                line we will construct.  Note that this value means the width
                rather than the number of characters (e.g., many East Asian
                characters expand to two columns).
            """
    result = self.line_length
    result -= line.depth * 4
    result -= 1 if ends_with_comma else 0
    result -= string_op_leaves_length
    exit(result)

# --- Calculate Max Break Width (for string value)
# We start with the line length limit
max_break_width = self.line_length
# The last index of a string of length N is N-1.
max_break_width -= 1
# Leading whitespace is not present in the string value (e.g. Leaf.value).
max_break_width -= line.depth * 4
if max_break_width < 0:
    exit(TErr(
        f"Unable to split {LL[string_idx].value} at such high of a line depth:"
        f" {line.depth}"
    ))
    exit()

# Check if StringMerger registered any custom splits.
custom_splits = self.pop_custom_splits(LL[string_idx].value)
# We use them ONLY if none of them would produce lines that exceed the
# line limit.
use_custom_breakpoints = bool(
    custom_splits
    and all(csplit.break_idx <= max_break_width for csplit in custom_splits)
)

# Temporary storage for the remaining chunk of the string line that
# can't fit onto the line currently being constructed.
rest_value = LL[string_idx].value

def more_splits_should_be_made() -> bool:
    """
            Returns:
                True iff `rest_value` (the remaining string value from the last
                split), should be split again.
            """
    if use_custom_breakpoints:
        exit(len(custom_splits) > 1)
    else:
        exit(str_width(rest_value) > max_last_string_column())

string_line_results: List[Ok[Line]] = []
while more_splits_should_be_made():
    if use_custom_breakpoints:
        # Custom User Split (manual)
        csplit = custom_splits.pop(0)
        break_idx = csplit.break_idx
    else:
        # Algorithmic Split (automatic)
        max_bidx = (
            count_chars_in_width(rest_value, max_break_width)
            - string_op_leaves_length
        )
        maybe_break_idx = self._get_break_idx(rest_value, max_bidx)
        if maybe_break_idx is None:
            # If we are unable to algorithmically determine a good split
            # and this string has custom splits registered to it, we
            # fall back to using them--which means we have to start
            # over from the beginning.
            if custom_splits:
                rest_value = LL[string_idx].value
                string_line_results = []
                first_string_line = True
                use_custom_breakpoints = True
                continue

            # Otherwise, we stop splitting here.
            break

        break_idx = maybe_break_idx

    # --- Construct `next_value`
    next_value = rest_value[:break_idx] + QUOTE

    # HACK: The following 'if' statement is a hack to fix the custom
    # breakpoint index in the case of either: (a) substrings that were
    # f-strings but will have the 'f' prefix removed OR (b) substrings
    # that were not f-strings but will now become f-strings because of
    # redundant use of the 'f' prefix (i.e. none of the substrings
    # contain f-expressions but one or more of them had the 'f' prefix
    # anyway; in which case, we will prepend 'f' to _all_ substrings).
    #
    # There is probably a better way to accomplish what is being done
    # here...
    #
    # If this substring is an f-string, we _could_ remove the 'f'
    # prefix, and the current custom split did NOT originally use a
    # prefix...
    if (
        use_custom_breakpoints
        and not csplit.has_prefix
        and (
            # `next_value == prefix + QUOTE` happens when the custom
            # split is an empty string.
            next_value == prefix + QUOTE
            or next_value != self._normalize_f_string(next_value, prefix)
        )
    ):
        # Then `csplit.break_idx` will be off by one after removing
        # the 'f' prefix.
        break_idx += 1
        next_value = rest_value[:break_idx] + QUOTE

    if drop_pointless_f_prefix:
        next_value = self._normalize_f_string(next_value, prefix)

    # --- Construct `next_leaf`
    next_leaf = Leaf(token.STRING, next_value)
    insert_str_child(next_leaf)
    self._maybe_normalize_string_quotes(next_leaf)

    # --- Construct `next_line`
    next_line = line.clone()
    maybe_append_string_operators(next_line)
    next_line.append(next_leaf)
    string_line_results.append(Ok(next_line))

    rest_value = prefix + QUOTE + rest_value[break_idx:]
    first_string_line = False

exit(string_line_results)

if drop_pointless_f_prefix:
    rest_value = self._normalize_f_string(rest_value, prefix)

rest_leaf = Leaf(token.STRING, rest_value)
insert_str_child(rest_leaf)

# NOTE: I could not find a test case that verifies that the following
# line is actually necessary, but it seems to be. Otherwise we risk
# not normalizing the last substring, right?
self._maybe_normalize_string_quotes(rest_leaf)

last_line = line.clone()
maybe_append_string_operators(last_line)

# If there are any leaves to the right of the target string...
if is_valid_index(string_idx + 1):
    # We use `temp_value` here to determine how long the last line
    # would be if we were to append all the leaves to the right of the
    # target string to the last string line.
    temp_value = rest_value
    for leaf in LL[string_idx + 1 :]:
        temp_value += str(leaf)
        if leaf.type == token.LPAR:
            break

    # Try to fit them all on the same line with the last substring...
    if (
        str_width(temp_value) <= max_last_string_column()
        or LL[string_idx + 1].type == token.COMMA
    ):
        last_line.append(rest_leaf)
        append_leaves(last_line, line, LL[string_idx + 1 :])
        exit(Ok(last_line))
    # Otherwise, place the last substring on one line and everything
    # else on a line below that...
    else:
        last_line.append(rest_leaf)
        exit(Ok(last_line))

        non_string_line = line.clone()
        append_leaves(non_string_line, line, LL[string_idx + 1 :])
        exit(Ok(non_string_line))
# Else the target string was the last leaf...
else:
    last_line.append(rest_leaf)
    last_line.comments = line.comments.copy()
    exit(Ok(last_line))
