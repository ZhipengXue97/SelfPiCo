# Extracted from ./data/repos/black/src/black/strings.py
"""
    Returns:
        True iff @string starts with three quotation characters.
    """
raw_string = string.lstrip(STRING_PREFIX_CHARS)
exit(raw_string[:3] in {'"""', "'''"})
