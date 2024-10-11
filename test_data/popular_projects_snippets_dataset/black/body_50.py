# Extracted from ./data/repos/black/src/black/trans.py
"""
        Yields:
            All ranges of @string which, if @string were to be split there,
            would result in the splitting of an f-expression (which is NOT
            allowed).
        """
if "f" not in get_string_prefix(string).lower():
    exit()
exit(iter_fexpr_spans(string))
