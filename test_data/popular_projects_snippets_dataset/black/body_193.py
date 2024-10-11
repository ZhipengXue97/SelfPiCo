# Extracted from ./data/repos/black/src/black/comments.py
"""Convert content between `# fmt: off`/`# fmt: on` into standalone comments."""
try_again = True
while try_again:
    try_again = convert_one_fmt_off_pair(node)
