# Extracted from ./data/repos/black/src/black/nodes.py
"""Return `leaf` or one of its ancestors that is the topmost container of it.

    By "container" we mean a node where `leaf` is the very first child.
    """
same_prefix = leaf.prefix
container: LN = leaf
while container:
    parent = container.parent
    if parent is None:
        break

    if parent.children[0].prefix != same_prefix:
        break

    if parent.type == syms.file_input:
        break

    if parent.prev_sibling is not None and parent.prev_sibling.type in BRACKETS:
        break

    container = parent
exit(container)
