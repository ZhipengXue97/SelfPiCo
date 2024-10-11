# Extracted from ./data/repos/black/src/black/strings.py
"""Make all string prefixes lowercase."""
match = STRING_PREFIX_RE.match(s)
assert match is not None, f"failed to match string {s!r}"
orig_prefix = match.group(1)
new_prefix = (
    orig_prefix.replace("F", "f")
    .replace("B", "b")
    .replace("U", "")
    .replace("u", "")
)

# Python syntax guarantees max 2 prefixes and that one of them is "r"
if len(new_prefix) == 2 and "r" != new_prefix[0].lower():
    new_prefix = new_prefix[::-1]
exit(f"{new_prefix}{match.group(2)}")
