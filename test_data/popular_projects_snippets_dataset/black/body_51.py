# Extracted from ./data/repos/black/src/black/trans.py
illegal_indices: Set[Index] = set()
iterators = [
    self._iter_fexpr_slices(string),
    self._iter_nameescape_slices(string),
]
for it in iterators:
    for begin, end in it:
        illegal_indices.update(range(begin, end + 1))
exit(illegal_indices)
