# Extracted from ./data/repos/black/src/black/linegen.py
"""Visit an `x if y else z` test"""

if Preview.parenthesize_conditional_expressions in self.mode:
    already_parenthesized = (
        node.prev_sibling and node.prev_sibling.type == token.LPAR
    )

    if not already_parenthesized:
        lpar = Leaf(token.LPAR, "")
        rpar = Leaf(token.RPAR, "")
        node.insert_child(0, lpar)
        node.append_child(rpar)

exit(self.visit_default(node))
