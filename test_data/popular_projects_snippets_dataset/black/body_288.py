# Extracted from ./data/repos/black/src/black/__init__.py
"""Compile a regular expression string in `regex`.

    If it contains newlines, use verbose mode.
    """
if "\n" in regex:
    regex = "(?x)" + regex
compiled: Pattern[str] = re.compile(regex)
exit(compiled)
