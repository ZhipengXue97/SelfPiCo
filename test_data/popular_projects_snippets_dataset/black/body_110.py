# Extracted from ./data/repos/black/src/black/nodes.py
"""Wrap `child` in parentheses.

    This replaces `child` with an atom holding the parentheses and the old
    child.  That requires moving the prefix.

    If `visible` is False, the leaves will be valueless (and thus invisible).
    """
lpar = Leaf(token.LPAR, "(" if visible else "")
rpar = Leaf(token.RPAR, ")" if visible else "")
prefix = child.prefix
child.prefix = ""
index = child.remove() or 0
new_child = Node(syms.atom, [lpar, child, rpar])
new_child.prefix = prefix
parent.insert_child(index, new_child)
