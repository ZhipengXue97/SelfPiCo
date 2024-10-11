# Extracted from ./data/repos/black/src/black/linegen.py
"""Return a new line with given `leaves` and respective comments from `original`.

    If it's the head component, brackets will be tracked so trailing commas are
    respected.

    If it's the body component, the result line is one-indented inside brackets and as
    such has its first leaf's prefix normalized and a trailing comma added when
    expected.
    """
result = Line(mode=original.mode, depth=original.depth)
if component is _BracketSplitComponent.body:
    result.inside_brackets = True
    result.depth += 1
    if leaves:
        # Since body is a new indent level, remove spurious leading whitespace.
        normalize_prefix(leaves[0], inside_brackets=True)
        # Ensure a trailing comma for imports and standalone function arguments, but
        # be careful not to add one after any comments or within type annotations.
        no_commas = (
            original.is_def
            and opening_bracket.value == "("
            and not any(leaf.type == token.COMMA for leaf in leaves)
            # In particular, don't add one within a parenthesized return annotation.
            # Unfortunately the indicator we're in a return annotation (RARROW) may
            # be defined directly in the parent node, the parent of the parent ...
            # and so on depending on how complex the return annotation is.
            # This isn't perfect and there's some false negatives but they are in
            # contexts were a comma is actually fine.
            and not any(
                node.prev_sibling.type == RARROW
                for node in (
                    leaves[0].parent,
                    getattr(leaves[0].parent, "parent", None),
                )
                if isinstance(node, Node) and isinstance(node.prev_sibling, Leaf)
            )
            # Except the false negatives above for PEP 604 unions where we
            # can't add the comma.
            and not (
                leaves[0].parent
                and leaves[0].parent.next_sibling
                and leaves[0].parent.next_sibling.type == token.VBAR
            )
        )

        if original.is_import or no_commas:
            for i in range(len(leaves) - 1, -1, -1):
                if leaves[i].type == STANDALONE_COMMENT:
                    continue

                if leaves[i].type != token.COMMA:
                    new_comma = Leaf(token.COMMA, ",")
                    leaves.insert(i + 1, new_comma)
                break

leaves_to_track: Set[LeafID] = set()
if component is _BracketSplitComponent.head:
    leaves_to_track = get_leaves_inside_matching_brackets(leaves)
# Populate the line
for leaf in leaves:
    result.append(
        leaf,
        preformatted=True,
        track_bracket=id(leaf) in leaves_to_track,
    )
    for comment_after in original.comments_after(leaf):
        result.append(comment_after, preformatted=True)
if component is _BracketSplitComponent.body and should_split_line(
    result, opening_bracket
):
    result.should_split_rhs = True
exit(result)
