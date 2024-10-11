# Extracted from ./data/repos/black/src/black/nodes.py
"""Returns whether this leaf is part of type annotations."""
ancestor = leaf.parent
while ancestor is not None:
    if ancestor.prev_sibling and ancestor.prev_sibling.type == token.RARROW:
        exit(True)
    if ancestor.parent and ancestor.parent.type == syms.tname:
        exit(True)
    ancestor = ancestor.parent
exit(False)
