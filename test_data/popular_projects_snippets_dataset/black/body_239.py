# Extracted from ./data/repos/black/src/black/linegen.py
"""Normalize prefix of the first leaf in every line returned by `split_func`.

    This is a decorator over relevant split functions.
    """

@wraps(split_func)
def split_wrapper(
    line: Line, features: Collection[Feature], mode: Mode
) -> Iterator[Line]:
    for split_line in split_func(line, features, mode):
        normalize_prefix(split_line.leaves[0], inside_brackets=True)
        exit(split_line)

exit(split_wrapper)
