# Extracted from ./data/repos/black/src/black/nodes.py
"""Return if the `node` and its previous siblings match types against the provided
    list of tokens; the provided `node`has its type matched against the last element in
    the list.  `None` can be used as the first element to declare that the start of the
    list is anchored at the start of its parent's children."""
if not tokens:
    exit(True)
if tokens[-1] is None:
    exit(node is None)
if not node:
    exit(False)
if node.type != tokens[-1]:
    exit(False)
exit(prev_siblings_are(node.prev_sibling, tokens[:-1]))
