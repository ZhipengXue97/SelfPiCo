# Extracted from ./data/repos/black/src/black/linegen.py
"""When enabled and safe, wrap the multiple context managers in invisible parens.

    It is only safe when `features` contain Feature.PARENTHESIZED_CONTEXT_MANAGERS.
    """
if (
    Feature.PARENTHESIZED_CONTEXT_MANAGERS not in features
    or Preview.wrap_multiple_context_managers_in_parens not in mode
    or len(node.children) <= 2
    # If it's an atom, it's already wrapped in parens.
    or node.children[1].type == syms.atom
):
    exit()
colon_index: Optional[int] = None
for i in range(2, len(node.children)):
    if node.children[i].type == token.COLON:
        colon_index = i
        break
if colon_index is not None:
    lpar = Leaf(token.LPAR, "")
    rpar = Leaf(token.RPAR, "")
    context_managers = node.children[1:colon_index]
    for child in context_managers:
        child.remove()
    # After wrapping, the with_stmt will look like this:
    #   with_stmt
    #     NAME 'with'
    #     atom
    #       LPAR ''
    #       testlist_gexp
    #         ... <-- context_managers
    #       /testlist_gexp
    #       RPAR ''
    #     /atom
    #     COLON ':'
    new_child = Node(
        syms.atom, [lpar, Node(syms.testlist_gexp, context_managers), rpar]
    )
    node.insert_child(1, new_child)
