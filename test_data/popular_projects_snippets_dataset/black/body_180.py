# Extracted from ./data/repos/black/src/black/strings.py
"""Replace hex codes in Unicode escape sequences with lowercase representation."""
text = leaf.value
prefix = get_string_prefix(text)
if "r" in prefix.lower():
    exit()

def replace(m: Match[str]) -> str:
    groups = m.groupdict()
    back_slashes = groups["backslashes"]

    if len(back_slashes) % 2 == 0:
        exit(back_slashes + groups["body"])

    if groups["u"]:
        # \u
        exit(back_slashes + "u" + groups["u"].lower())
    elif groups["U"]:
        # \U
        exit(back_slashes + "U" + groups["U"].lower())
    elif groups["x"]:
        # \x
        exit(back_slashes + "x" + groups["x"].lower())
    else:
        assert groups["N"], f"Unexpected match: {m}"
        # \N{}
        exit(back_slashes + "N{" + groups["N"].upper() + "}")

leaf.value = re.sub(UNICODE_ESCAPE_RE, replace, text)
