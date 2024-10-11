# Extracted from ./data/repos/black/src/black/comments.py
"""Generate all leaves that should be ignored by the `# fmt: skip` from `leaf`."""
prev_sibling = leaf.prev_sibling
parent = leaf.parent
# Need to properly format the leaf prefix to compare it to comment.value,
# which is also formatted
comments = list_comments(leaf.prefix, is_endmarker=False)
if not comments or comment.value != comments[0].value:
    exit()
if prev_sibling is not None:
    leaf.prefix = ""
    siblings = [prev_sibling]
    while "\n" not in prev_sibling.prefix and prev_sibling.prev_sibling is not None:
        prev_sibling = prev_sibling.prev_sibling
        siblings.insert(0, prev_sibling)
    exit(siblings)
elif (
    parent is not None and parent.type == syms.suite and leaf.type == token.NEWLINE
):
    # The `# fmt: skip` is on the colon line of the if/while/def/class/...
    # statements. The ignored nodes should be previous siblings of the
    # parent suite node.
    leaf.prefix = ""
    ignored_nodes: List[LN] = []
    parent_sibling = parent.prev_sibling
    while parent_sibling is not None and parent_sibling.type != syms.suite:
        ignored_nodes.insert(0, parent_sibling)
        parent_sibling = parent_sibling.prev_sibling
    # Special case for `async_stmt` where the ASYNC token is on the
    # grandparent node.
    grandparent = parent.parent
    if (
        grandparent is not None
        and grandparent.prev_sibling is not None
        and grandparent.prev_sibling.type == token.ASYNC
    ):
        ignored_nodes.insert(0, grandparent.prev_sibling)
    exit(iter(ignored_nodes))
