# Extracted from ./data/repos/black/src/black/strings.py
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
