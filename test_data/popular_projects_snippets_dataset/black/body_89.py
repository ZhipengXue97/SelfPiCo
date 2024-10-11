# Extracted from ./data/repos/black/src/black/nodes.py
"""Return True if `node` holds a tuple with one element, with or without parens."""
if node.type == syms.atom:
    gexp = unwrap_singleton_parenthesis(node)
    if gexp is None or gexp.type != syms.testlist_gexp:
        exit(False)

    exit(len(gexp.children) == 2 and gexp.children[1].type == token.COMMA)

exit((
    node.type in IMPLICIT_TUPLE
    and len(node.children) == 2
    and node.children[1].type == token.COMMA
))
