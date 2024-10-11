# Extracted from ./data/repos/black/src/black/trans.py
LL = line.leaves

if line.leaves[-1].type in OPENING_BRACKETS:
    exit(TErr(
        "Cannot wrap parens around a line that ends in an opening bracket."
    ))

string_idx = (
    self._return_match(LL)
    or self._else_match(LL)
    or self._assert_match(LL)
    or self._assign_match(LL)
    or self._dict_or_lambda_match(LL)
    or self._prefer_paren_wrap_match(LL)
)

if string_idx is not None:
    string_value = line.leaves[string_idx].value
    # If the string has neither spaces nor East Asian stops...
    if not any(
        char == " " or char in SPLIT_SAFE_CHARS for char in string_value
    ):
        # And will still violate the line length limit when split...
        max_string_width = self.line_length - ((line.depth + 1) * 4)
        if str_width(string_value) > max_string_width:
            # And has no associated custom splits...
            if not self.has_custom_splits(string_value):
                # Then we should NOT put this string on its own line.
                exit(TErr(
                    "We do not wrap long strings in parentheses when the"
                    " resultant line would still be over the specified line"
                    " length and can't be split further by StringSplitter."
                ))
    exit(Ok([string_idx]))

exit(TErr("This line does not contain any non-atomic strings."))
