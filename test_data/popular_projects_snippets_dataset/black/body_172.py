# Extracted from ./data/repos/black/src/black/strings.py
"""
    Splits string into lines and expands only leading tabs (following the normal
    Python rules)
    """
lines = []
for line in s.splitlines():
    # Find the index of the first non-whitespace character after a string of
    # whitespace that includes at least one tab
    match = FIRST_NON_WHITESPACE_RE.match(line)
    if match:
        first_non_whitespace_idx = match.start(1)

        lines.append(
            line[:first_non_whitespace_idx].expandtabs()
            + line[first_non_whitespace_idx:]
        )
    else:
        lines.append(line)
exit(lines)
