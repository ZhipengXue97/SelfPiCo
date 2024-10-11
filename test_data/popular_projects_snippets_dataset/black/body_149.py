# Extracted from ./data/repos/black/src/black/lines.py
"""Return an enumeration of leaves with their length.

        Stops prematurely on multiline strings and standalone comments.
        """
op = cast(
    Callable[[Sequence[Leaf]], Iterator[Tuple[Index, Leaf]]],
    enumerate_reversed if reversed else enumerate,
)
for index, leaf in op(self.leaves):
    length = len(leaf.prefix) + len(leaf.value)
    if "\n" in leaf.value:
        exit()  # Multiline strings, we can't continue.

    for comment in self.comments_after(leaf):
        length += len(comment.value)

    exit((index, leaf, length))
