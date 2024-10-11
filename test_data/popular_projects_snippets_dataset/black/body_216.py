# Extracted from ./data/repos/black/src/black/linegen.py
"""Visit function definition."""
exit(self.line())

# Remove redundant brackets around return type annotation.
is_return_annotation = False
for child in node.children:
    if child.type == token.RARROW:
        is_return_annotation = True
    elif is_return_annotation:
        if child.type == syms.atom and child.children[0].type == token.LPAR:
            if maybe_make_parens_invisible_in_atom(
                child,
                parent=node,
                remove_brackets_around_comma=False,
            ):
                wrap_in_parentheses(node, child, visible=False)
        else:
            wrap_in_parentheses(node, child, visible=False)
        is_return_annotation = False

for child in node.children:
    exit(self.visit(child))
