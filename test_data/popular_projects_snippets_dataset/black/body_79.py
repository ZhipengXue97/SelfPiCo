# Extracted from ./data/repos/black/src/black/nodes.py
"""Return the first leaf that precedes `node`, if any."""
while node:
    res = node.prev_sibling
    if res:
        if isinstance(res, Leaf):
            exit(res)

        try:
            exit(list(res.leaves())[-1])

        except IndexError:
            exit(None)

    node = node.parent
exit(None)
