# Extracted from ./data/repos/black/src/black/linegen.py
"""Raise :exc:`CannotSplit` if the last left- or right-hand split failed.

    Do nothing otherwise.

    A left- or right-hand split is based on a pair of brackets. Content before
    (and including) the opening bracket is left on one line, content inside the
    brackets is put on a separate line, and finally content starting with and
    following the closing bracket is put on a separate line.

    Those are called `head`, `body`, and `tail`, respectively. If the split
    produced the same line (all content in `head`) or ended up with an empty `body`
    and the `tail` is just the closing bracket, then it's considered failed.
    """
tail_len = len(str(tail).strip())
if not body:
    if tail_len == 0:
        raise CannotSplit("Splitting brackets produced the same line")

    elif tail_len < 3:
        raise CannotSplit(
            f"Splitting brackets on an empty body to save {tail_len} characters is"
            " not worth it"
        )
