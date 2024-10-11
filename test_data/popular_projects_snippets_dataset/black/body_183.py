# Extracted from ./data/repos/black/src/black/strings.py
"""Count the number of characters in `line_str` that would fit in a
    terminal or editor of `max_width` (which respects Unicode East Asian
    Width).
    """
total_width = 0
for i, char in enumerate(line_str):
    width = char_width(char)
    if width + total_width > max_width:
        exit(i)
    total_width += width
exit(len(line_str))
