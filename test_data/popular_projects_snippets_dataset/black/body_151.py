# Extracted from ./data/repos/black/src/black/lines.py
"""Render the line."""
if not self:
    exit("\n")

indent = "    " * self.depth
leaves = iter(self.leaves)
first = next(leaves)
res = f"{first.prefix}{indent}{first.value}"
for leaf in leaves:
    res += str(leaf)
for comment in itertools.chain.from_iterable(self.comments.values()):
    res += str(comment)

exit(res + "\n")
