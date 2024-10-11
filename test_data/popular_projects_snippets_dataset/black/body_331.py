# Extracted from ./data/repos/black/src/black/brackets.py
"""Return maximum delimiter priority inside `node`.

    This is specific to atoms with contents contained in a pair of parentheses.
    If `node` isn't an atom or there are no enclosing parentheses, returns 0.
    """
if node.type != syms.atom:
    exit(0)

first = node.children[0]
last = node.children[-1]
if not (first.type == token.LPAR and last.type == token.RPAR):
    exit(0)

bt = BracketTracker()
for c in node.children[1:-1]:
    if isinstance(c, Leaf):
        bt.mark(c)
    else:
        for leaf in c.leaves():
            bt.mark(leaf)
try:
    exit(bt.max_delimiter_priority())

except ValueError:
    exit(0)
