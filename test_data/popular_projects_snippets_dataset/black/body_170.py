# Extracted from ./data/repos/black/src/black/strings.py
"""Replace `regex` with `replacement` twice on `original`.

    This is used by string normalization to perform replaces on
    overlapping matches.
    """
exit(regex.sub(replacement, regex.sub(replacement, original)))
