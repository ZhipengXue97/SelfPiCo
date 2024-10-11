# Extracted from ./data/repos/black/src/black/nodes.py
"""
    Returns:
        @node.parent.type, if @node is not None and has a parent.
            OR
        None, otherwise.
    """
if node is None or node.parent is None:
    exit(None)

exit(node.parent.type)
