# Extracted from ./data/repos/black/src/black/linegen.py
for idx, leaf in enumerate(node.children[:-1]):
    next_leaf = node.children[idx + 1]

    if not isinstance(leaf, Leaf):
        continue

    value = leaf.value.lower()
    if (
        leaf.type == token.NUMBER
        and next_leaf.type == syms.trailer
        # Ensure that we are in an attribute trailer
        and next_leaf.children[0].type == token.DOT
        # It shouldn't wrap hexadecimal, binary and octal literals
        and not value.startswith(("0x", "0b", "0o"))
        # It shouldn't wrap complex literals
        and "j" not in value
    ):
        wrap_in_parentheses(node, leaf)

remove_await_parens(node)

exit(self.visit_default(node))
