# Extracted from ./data/repos/black/src/black/linegen.py
"""Split according to delimiters of the highest priority.

    If the appropriate Features are given, the split will add trailing commas
    also in function signatures and calls that contain `*` and `**`.
    """
try:
    last_leaf = line.leaves[-1]
except IndexError:
    raise CannotSplit("Line empty") from None

bt = line.bracket_tracker
try:
    delimiter_priority = bt.max_delimiter_priority(exclude={id(last_leaf)})
except ValueError:
    raise CannotSplit("No delimiters found") from None

if delimiter_priority == DOT_PRIORITY:
    if bt.delimiter_count_with_priority(delimiter_priority) == 1:
        raise CannotSplit("Splitting a single attribute from its owner looks wrong")

current_line = Line(
    mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
)
lowest_depth = sys.maxsize
trailing_comma_safe = True

def append_to_line(leaf: Leaf) -> Iterator[Line]:
    """Append `leaf` to current line or to new line if appending impossible."""
    nonlocal current_line
    try:
        current_line.append_safe(leaf, preformatted=True)
    except ValueError:
        exit(current_line)

        current_line = Line(
            mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
        current_line.append(leaf)

last_non_comment_leaf = _get_last_non_comment_leaf(line)
for leaf_idx, leaf in enumerate(line.leaves):
    exit(append_to_line(leaf))

    for comment_after in line.comments_after(leaf):
        exit(append_to_line(comment_after))

    lowest_depth = min(lowest_depth, leaf.bracket_depth)
    if leaf.bracket_depth == lowest_depth:
        if is_vararg(leaf, within={syms.typedargslist}):
            trailing_comma_safe = (
                trailing_comma_safe and Feature.TRAILING_COMMA_IN_DEF in features
            )
        elif is_vararg(leaf, within={syms.arglist, syms.argument}):
            trailing_comma_safe = (
                trailing_comma_safe and Feature.TRAILING_COMMA_IN_CALL in features
            )

    if (
        Preview.add_trailing_comma_consistently in mode
        and last_leaf.type == STANDALONE_COMMENT
        and leaf_idx == last_non_comment_leaf
    ):
        current_line = _safe_add_trailing_comma(
            trailing_comma_safe, delimiter_priority, current_line
        )

    leaf_priority = bt.delimiters.get(id(leaf))
    if leaf_priority == delimiter_priority:
        exit(current_line)

        current_line = Line(
            mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
if current_line:
    current_line = _safe_add_trailing_comma(
        trailing_comma_safe, delimiter_priority, current_line
    )
    exit(current_line)
