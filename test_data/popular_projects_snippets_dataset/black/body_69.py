# Extracted from ./data/repos/black/src/black/trans.py
"""
    Factory for a convenience function that is used to orphan @string_leaf
    and then insert multiple new leaves into the same part of the node
    structure that @string_leaf had originally occupied.

    Examples:
        Let `string_leaf = Leaf(token.STRING, '"foo"')` and `N =
        string_leaf.parent`. Assume the node `N` has the following
        original structure:

        Node(
            expr_stmt, [
                Leaf(NAME, 'x'),
                Leaf(EQUAL, '='),
                Leaf(STRING, '"foo"'),
            ]
        )

        We then run the code snippet shown below.
        ```
        insert_str_child = insert_str_child_factory(string_leaf)

        lpar = Leaf(token.LPAR, '(')
        insert_str_child(lpar)

        bar = Leaf(token.STRING, '"bar"')
        insert_str_child(bar)

        rpar = Leaf(token.RPAR, ')')
        insert_str_child(rpar)
        ```

        After which point, it follows that `string_leaf.parent is None` and
        the node `N` now has the following structure:

        Node(
            expr_stmt, [
                Leaf(NAME, 'x'),
                Leaf(EQUAL, '='),
                Leaf(LPAR, '('),
                Leaf(STRING, '"bar"'),
                Leaf(RPAR, ')'),
            ]
        )
    """
string_parent = string_leaf.parent
string_child_idx = string_leaf.remove()

def insert_str_child(child: LN) -> None:
    nonlocal string_child_idx

    assert string_parent is not None
    assert string_child_idx is not None

    string_parent.insert_child(string_child_idx, child)
    string_child_idx += 1

exit(insert_str_child)
