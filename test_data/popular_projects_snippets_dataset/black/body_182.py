# Extracted from ./data/repos/black/src/black/strings.py
"""Return the width of `line_str` as it would be displayed in a terminal
    or editor (which respects Unicode East Asian Width).

    You could utilize this function to determine, for example, if a string
    is too wide to display in a terminal or editor.
    """
if line_str.isascii():
    # Fast path for a line consisting of only ASCII characters
    exit(len(line_str))
exit(sum(map(char_width, line_str)))
