# Extracted from ./data/repos/black/src/black/linegen.py
"""Make existing optional parentheses invisible or create new ones.

    `parens_after` is a set of string leaf values immediately after which parens
    should be put.

    Standardizes on visible parentheses for single-element tuples, and keeps
    existing visible parentheses for other tuples and generator expressions.
    """
for pc in list_comments(node.prefix, is_endmarker=False):
    if pc.value in FMT_OFF:
        # This `node` has a prefix with `# fmt: off`, don't mess with parens.
        exit()

# The multiple context managers grammar has a different pattern, thus this is
# separate from the for-loop below. This possibly wraps them in invisible parens,
# and later will be removed in remove_with_parens when needed.
if node.type == syms.with_stmt:
    _maybe_wrap_cms_in_parens(node, mode, features)

check_lpar = False
for index, child in enumerate(list(node.children)):
    # Fixes a bug where invisible parens are not properly stripped from
    # assignment statements that contain type annotations.
    if isinstance(child, Node) and child.type == syms.annassign:
        normalize_invisible_parens(
            child, parens_after=parens_after, mode=mode, features=features
        )

    # Add parentheses around long tuple unpacking in assignments.
    if (
        index == 0
        and isinstance(child, Node)
        and child.type == syms.testlist_star_expr
    ):
        check_lpar = True

    if check_lpar:
        if (
            child.type == syms.atom
            and node.type == syms.for_stmt
            and isinstance(child.prev_sibling, Leaf)
            and child.prev_sibling.type == token.NAME
            and child.prev_sibling.value == "for"
        ):
            if maybe_make_parens_invisible_in_atom(
                child,
                parent=node,
                remove_brackets_around_comma=True,
            ):
                wrap_in_parentheses(node, child, visible=False)
        elif isinstance(child, Node) and node.type == syms.with_stmt:
            remove_with_parens(child, node)
        elif child.type == syms.atom:
            if maybe_make_parens_invisible_in_atom(
                child,
                parent=node,
            ):
                wrap_in_parentheses(node, child, visible=False)
        elif is_one_tuple(child):
            wrap_in_parentheses(node, child, visible=True)
        elif node.type == syms.import_from:
            _normalize_import_from(node, child, index)
            break
        elif (
            index == 1
            and child.type == token.STAR
            and node.type == syms.except_clause
        ):
            # In except* (PEP 654), the star is actually part of
            # of the keyword. So we need to skip the insertion of
            # invisible parentheses to work more precisely.
            continue

        elif not (isinstance(child, Leaf) and is_multiline_string(child)):
            wrap_in_parentheses(node, child, visible=False)

    comma_check = child.type == token.COMMA

    check_lpar = isinstance(child, Leaf) and (
        child.value in parens_after or comma_check
    )
