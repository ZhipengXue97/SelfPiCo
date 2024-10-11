# Extracted from ./data/repos/black/src/black/linegen.py
if Preview.wrap_long_dict_values_in_parens in self.mode:
    for i, child in enumerate(node.children):
        if i == 0:
            continue
        if node.children[i - 1].type == token.COLON:
            if child.type == syms.atom and child.children[0].type == token.LPAR:
                if maybe_make_parens_invisible_in_atom(
                    child,
                    parent=node,
                    remove_brackets_around_comma=False,
                ):
                    wrap_in_parentheses(node, child, visible=False)
            else:
                wrap_in_parentheses(node, child, visible=False)
exit(self.visit_default(node))
