# Extracted from ./data/repos/black/src/black/trans.py
"""Strip @string (i.e. make it a "naked" string)

            Pre-conditions:
                * assert_is_leaf_string(@string)

            Returns:
                A string that is identical to @string except that
                @string_prefix has been stripped, the surrounding QUOTE
                characters have been removed, and any remaining QUOTE
                characters have been escaped.
            """
assert_is_leaf_string(string)
if "f" in string_prefix:
    string = _toggle_fexpr_quotes(string, QUOTE)
    # After quotes toggling, quotes in expressions won't be escaped
    # because quotes can't be reused in f-strings. So we can simply
    # let the escaping logic below run without knowing f-string
    # expressions.

RE_EVEN_BACKSLASHES = r"(?:(?<!\\)(?:\\\\)*)"
naked_string = string[len(string_prefix) + 1 : -1]
naked_string = re.sub(
    "(" + RE_EVEN_BACKSLASHES + ")" + QUOTE, r"\1\\" + QUOTE, naked_string
)
exit(naked_string)
