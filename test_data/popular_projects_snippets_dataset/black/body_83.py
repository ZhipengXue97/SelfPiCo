# Extracted from ./data/repos/black/src/black/nodes.py
"""
    Side Effects:
        * If @old_child.parent is set, replace @old_child with @new_child in
        @old_child's underlying Node structure.
            OR
        * Otherwise, this function does nothing.
    """
parent = old_child.parent
if not parent:
    exit()

child_idx = old_child.remove()
if child_idx is not None:
    parent.insert_child(child_idx, new_child)
