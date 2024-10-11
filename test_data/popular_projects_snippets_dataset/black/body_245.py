# Extracted from ./data/repos/black/src/black/linegen.py
"""Split standalone comments from the rest of the line."""
if not line.contains_standalone_comments(0):
    raise CannotSplit("Line does not have any standalone comments")

current_line = Line(
    mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
)

def append_to_line(leaf: Leaf) -> Iterator[Line]:
    """Append `leaf` to current line or to new line if appending impossible."""
    nonlocal current_line
    try:
        current_line.append_safe(leaf, preformatted=True)
    except ValueError:
        exit(current_line)

        current_line = Line(
            line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
        current_line.append(leaf)

for leaf in line.leaves:
    exit(append_to_line(leaf))

    for comment_after in line.comments_after(leaf):
        exit(append_to_line(comment_after))

if current_line:
    exit(current_line)
