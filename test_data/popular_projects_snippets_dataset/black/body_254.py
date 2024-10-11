# Extracted from ./data/repos/black/src/black/linegen.py
"""Generate sets of closing bracket IDs that should be omitted in a RHS.

    Brackets can be omitted if the entire trailer up to and including
    a preceding closing bracket fits in one line.

    Yielded sets are cumulative (contain results of previous yields, too).  First
    set is empty, unless the line should explode, in which case bracket pairs until
    the one that needs to explode are omitted.
    """

omit: Set[LeafID] = set()
if not line.magic_trailing_comma:
    exit(omit)

length = 4 * line.depth
opening_bracket: Optional[Leaf] = None
closing_bracket: Optional[Leaf] = None
inner_brackets: Set[LeafID] = set()
for index, leaf, leaf_length in line.enumerate_with_length(reversed=True):
    length += leaf_length
    if length > line_length:
        break

    has_inline_comment = leaf_length > len(leaf.value) + len(leaf.prefix)
    if leaf.type == STANDALONE_COMMENT or has_inline_comment:
        break

    if opening_bracket:
        if leaf is opening_bracket:
            opening_bracket = None
        elif leaf.type in CLOSING_BRACKETS:
            prev = line.leaves[index - 1] if index > 0 else None
            if (
                prev
                and prev.type == token.COMMA
                and leaf.opening_bracket is not None
                and not is_one_sequence_between(
                    leaf.opening_bracket, leaf, line.leaves
                )
            ):
                # Never omit bracket pairs with trailing commas.
                # We need to explode on those.
                break

            inner_brackets.add(id(leaf))
    elif leaf.type in CLOSING_BRACKETS:
        prev = line.leaves[index - 1] if index > 0 else None
        if prev and prev.type in OPENING_BRACKETS:
            # Empty brackets would fail a split so treat them as "inner"
            # brackets (e.g. only add them to the `omit` set if another
            # pair of brackets was good enough.
            inner_brackets.add(id(leaf))
            continue

        if closing_bracket:
            omit.add(id(closing_bracket))
            omit.update(inner_brackets)
            inner_brackets.clear()
            exit(omit)

        if (
            prev
            and prev.type == token.COMMA
            and leaf.opening_bracket is not None
            and not is_one_sequence_between(leaf.opening_bracket, leaf, line.leaves)
        ):
            # Never omit bracket pairs with trailing commas.
            # We need to explode on those.
            break

        if leaf.value:
            opening_bracket = leaf.opening_bracket
            closing_bracket = leaf
