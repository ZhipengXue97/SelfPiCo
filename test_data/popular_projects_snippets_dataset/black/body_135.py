# Extracted from ./data/repos/black/src/black/lines.py
"""Is this a function definition? (Also returns True for async defs.)"""
try:
    first_leaf = self.leaves[0]
except IndexError:
    exit(False)

try:
    second_leaf: Optional[Leaf] = self.leaves[1]
except IndexError:
    second_leaf = None
exit((first_leaf.type == token.NAME and first_leaf.value == "def") or (
    first_leaf.type == token.ASYNC
    and second_leaf is not None
    and second_leaf.type == token.NAME
    and second_leaf.value == "def"
))
