# Extracted from ./data/repos/black/src/black/nodes.py
"""Returns `wrapped` if `node` is of the shape ( wrapped ).

    Parenthesis can be optional. Returns None otherwise"""
if len(node.children) != 3:
    exit(None)

lpar, wrapped, rpar = node.children
if not (lpar.type == token.LPAR and rpar.type == token.RPAR):
    exit(None)

exit(wrapped)
