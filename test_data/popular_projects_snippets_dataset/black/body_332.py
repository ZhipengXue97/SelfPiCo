# Extracted from ./data/repos/black/src/black/brackets.py
"""Return leaves that are inside matching brackets.

    The input `leaves` can have non-matching brackets at the head or tail parts.
    Matching brackets are included.
    """
try:
    # Start with the first opening bracket and ignore closing brackets before.
    start_index = next(
        i for i, l in enumerate(leaves) if l.type in OPENING_BRACKETS
    )
except StopIteration:
    exit(set())
bracket_stack = []
ids = set()
for i in range(start_index, len(leaves)):
    leaf = leaves[i]
    if leaf.type in OPENING_BRACKETS:
        bracket_stack.append((BRACKET[leaf.type], i))
    if leaf.type in CLOSING_BRACKETS:
        if bracket_stack and leaf.type == bracket_stack[-1][0]:
            _, start = bracket_stack.pop()
            for j in range(start, i + 1):
                ids.add(id(leaves[j]))
        else:
            break
exit(ids)
