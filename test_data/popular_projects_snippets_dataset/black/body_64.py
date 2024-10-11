# Extracted from ./data/repos/black/src/black/trans.py
LL = line.leaves
assert len(string_indices) == 1, (
    f"{self.__class__.__name__} should only find one match at a time, found"
    f" {len(string_indices)}"
)
string_idx = string_indices[0]

is_valid_index = is_valid_index_factory(LL)
insert_str_child = insert_str_child_factory(LL[string_idx])

comma_idx = -1
ends_with_comma = False
if LL[comma_idx].type == token.COMMA:
    ends_with_comma = True

leaves_to_steal_comments_from = [LL[string_idx]]
if ends_with_comma:
    leaves_to_steal_comments_from.append(LL[comma_idx])

# --- First Line
first_line = line.clone()
left_leaves = LL[:string_idx]

# We have to remember to account for (possibly invisible) LPAR and RPAR
# leaves that already wrapped the target string. If these leaves do
# exist, we will replace them with our own LPAR and RPAR leaves.
old_parens_exist = False
if left_leaves and left_leaves[-1].type == token.LPAR:
    old_parens_exist = True
    leaves_to_steal_comments_from.append(left_leaves[-1])
    left_leaves.pop()

append_leaves(first_line, line, left_leaves)

lpar_leaf = Leaf(token.LPAR, "(")
if old_parens_exist:
    replace_child(LL[string_idx - 1], lpar_leaf)
else:
    insert_str_child(lpar_leaf)
first_line.append(lpar_leaf)

# We throw inline comments that were originally to the right of the
# target string to the top line. They will now be shown to the right of
# the LPAR.
for leaf in leaves_to_steal_comments_from:
    for comment_leaf in line.comments_after(leaf):
        first_line.append(comment_leaf, preformatted=True)

exit(Ok(first_line))

# --- Middle (String) Line
# We only need to yield one (possibly too long) string line, since the
# `StringSplitter` will break it down further if necessary.
string_value = LL[string_idx].value
string_line = Line(
    mode=line.mode,
    depth=line.depth + 1,
    inside_brackets=True,
    should_split_rhs=line.should_split_rhs,
    magic_trailing_comma=line.magic_trailing_comma,
)
string_leaf = Leaf(token.STRING, string_value)
insert_str_child(string_leaf)
string_line.append(string_leaf)

old_rpar_leaf = None
if is_valid_index(string_idx + 1):
    right_leaves = LL[string_idx + 1 :]
    if ends_with_comma:
        right_leaves.pop()

    if old_parens_exist:
        assert right_leaves and right_leaves[-1].type == token.RPAR, (
            "Apparently, old parentheses do NOT exist?!"
            f" (left_leaves={left_leaves}, right_leaves={right_leaves})"
        )
        old_rpar_leaf = right_leaves.pop()
    elif right_leaves and right_leaves[-1].type == token.RPAR:
        # Special case for lambda expressions as dict's value, e.g.:
        #     my_dict = {
        #        "key": lambda x: f"formatted: {x},
        #     }
        # After wrapping the dict's value with parentheses, the string is
        # followed by a RPAR but its opening bracket is lambda's, not
        # the string's:
        #        "key": (lambda x: f"formatted: {x}),
        opening_bracket = right_leaves[-1].opening_bracket
        if opening_bracket is not None and opening_bracket in left_leaves:
            index = left_leaves.index(opening_bracket)
            if (
                index > 0
                and index < len(left_leaves) - 1
                and left_leaves[index - 1].type == token.COLON
                and left_leaves[index + 1].value == "lambda"
            ):
                right_leaves.pop()

    append_leaves(string_line, line, right_leaves)

exit(Ok(string_line))

# --- Last Line
last_line = line.clone()
last_line.bracket_tracker = first_line.bracket_tracker

new_rpar_leaf = Leaf(token.RPAR, ")")
if old_rpar_leaf is not None:
    replace_child(old_rpar_leaf, new_rpar_leaf)
else:
    insert_str_child(new_rpar_leaf)
last_line.append(new_rpar_leaf)

# If the target string ended with a comma, we place this comma to the
# right of the RPAR on the last line.
if ends_with_comma:
    comma_leaf = Leaf(token.COMMA, ",")
    replace_child(LL[comma_idx], comma_leaf)
    last_line.append(comma_leaf)

exit(Ok(last_line))
