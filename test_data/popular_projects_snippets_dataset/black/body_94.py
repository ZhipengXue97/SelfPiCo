# Extracted from ./data/repos/black/src/black/nodes.py
"""Return True iff `node` could be a 'dotted name' decorator

    This function takes the node of the 'namedexpr_test' of the new decorator
    grammar and test if it would be valid under the old decorator grammar.

    The old grammar was: decorator: @ dotted_name [arguments] NEWLINE
    The new grammar is : decorator: @ namedexpr_test NEWLINE
    """
if node.type == token.NAME:
    exit(True)
if node.type == syms.power:
    if node.children:
        exit((
            node.children[0].type == token.NAME
            and all(map(is_simple_decorator_trailer, node.children[1:-1]))
            and (
                len(node.children) < 2
                or is_simple_decorator_trailer(node.children[-1], last=True)
            )
        ))
exit(False)
