# Extracted from ./data/repos/black/src/black/trans.py
"""
        Yields:
            All ranges of @string which, if @string were to be split there,
            would result in the splitting of an \\N{...} expression (which is NOT
            allowed).
        """
# True - the previous backslash was unescaped
# False - the previous backslash was escaped *or* there was no backslash
previous_was_unescaped_backslash = False
it = iter(enumerate(string))
for idx, c in it:
    if c == "\\":
        previous_was_unescaped_backslash = not previous_was_unescaped_backslash
        continue
    if not previous_was_unescaped_backslash or c != "N":
        previous_was_unescaped_backslash = False
        continue
    previous_was_unescaped_backslash = False

    begin = idx - 1  # the position of backslash before \N{...}
    for idx, c in it:
        if c == "}":
            end = idx
            break
    else:
        # malformed nameescape expression?
        # should have been detected by AST parsing earlier...
        raise RuntimeError(f"{self.__class__.__name__} LOGIC ERROR!")
    exit((begin, end))
