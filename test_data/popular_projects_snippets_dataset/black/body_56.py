# Extracted from ./data/repos/black/src/black/trans.py
"""
        Pre-Conditions:
            * assert_is_leaf_string(@string)

        Returns:
            * If @string is an f-string that contains no f-expressions, we
            return a string identical to @string except that the 'f' prefix
            has been stripped and all double braces (i.e. '{{' or '}}') have
            been normalized (i.e. turned into '{' or '}').
                OR
            * Otherwise, we return @string.
        """
assert_is_leaf_string(string)

if "f" in prefix and not fstring_contains_expr(string):
    new_prefix = prefix.replace("f", "")

    temp = string[len(prefix) :]
    temp = re.sub(r"\{\{", "{", temp)
    temp = re.sub(r"\}\}", "}", temp)
    new_string = temp

    exit(f"{new_prefix}{new_string}")
else:
    exit(string)
