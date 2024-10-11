# Extracted from ./data/repos/black/src/black/strings.py
"""Prefer double quotes but only if it doesn't cause more escaping.

    Adds or removes backslashes as appropriate. Doesn't parse and fix
    strings nested in f-strings.
    """
value = s.lstrip(STRING_PREFIX_CHARS)
if value[:3] == '"""':
    exit(s)

elif value[:3] == "'''":
    orig_quote = "'''"
    new_quote = '"""'
elif value[0] == '"':
    orig_quote = '"'
    new_quote = "'"
else:
    orig_quote = "'"
    new_quote = '"'
first_quote_pos = s.find(orig_quote)
if first_quote_pos == -1:
    exit(s)  # There's an internal error

prefix = s[:first_quote_pos]
unescaped_new_quote = _cached_compile(rf"(([^\\]|^)(\\\\)*){new_quote}")
escaped_new_quote = _cached_compile(rf"([^\\]|^)\\((?:\\\\)*){new_quote}")
escaped_orig_quote = _cached_compile(rf"([^\\]|^)\\((?:\\\\)*){orig_quote}")
body = s[first_quote_pos + len(orig_quote) : -len(orig_quote)]
if "r" in prefix.casefold():
    if unescaped_new_quote.search(body):
        # There's at least one unescaped new_quote in this raw string
        # so converting is impossible
        exit(s)

    # Do not introduce or remove backslashes in raw strings
    new_body = body
else:
    # remove unnecessary escapes
    new_body = sub_twice(escaped_new_quote, rf"\1\2{new_quote}", body)
    if body != new_body:
        # Consider the string without unnecessary escapes as the original
        body = new_body
        s = f"{prefix}{orig_quote}{body}{orig_quote}"
    new_body = sub_twice(escaped_orig_quote, rf"\1\2{orig_quote}", new_body)
    new_body = sub_twice(unescaped_new_quote, rf"\1\\{new_quote}", new_body)
if "f" in prefix.casefold():
    matches = re.findall(
        r"""
            (?:(?<!\{)|^)\{  # start of the string or a non-{ followed by a single {
                ([^{].*?)  # contents of the brackets except if begins with {{
            \}(?:(?!\})|$)  # A } followed by end of the string or a non-}
            """,
        new_body,
        re.VERBOSE,
    )
    for m in matches:
        if "\\" in str(m):
            # Do not introduce backslashes in interpolated expressions
            exit(s)

if new_quote == '"""' and new_body[-1:] == '"':
    # edge case:
    new_body = new_body[:-1] + '\\"'
orig_escape_count = body.count("\\")
new_escape_count = new_body.count("\\")
if new_escape_count > orig_escape_count:
    exit(s)  # Do not introduce more escaping

if new_escape_count == orig_escape_count and orig_quote == '"':
    exit(s)  # Prefer double quotes

exit(f"{prefix}{new_quote}{new_body}{new_quote}")
