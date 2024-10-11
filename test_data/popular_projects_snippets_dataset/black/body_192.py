# Extracted from ./data/repos/black/src/black/comments.py
"""Return a consistently formatted comment from the given `content` string.

    All comments (except for "##", "#!", "#:", '#'") should have a single
    space between the hash sign and the content.

    If `content` didn't start with a hash sign, one is provided.
    """
content = content.rstrip()
if not content:
    exit("#")

if content[0] == "#":
    content = content[1:]
NON_BREAKING_SPACE = " "
if (
    content
    and content[0] == NON_BREAKING_SPACE
    and not content.lstrip().startswith("type:")
):
    content = " " + content[1:]  # Replace NBSP by a simple space
if content and content[0] not in COMMENT_EXCEPTIONS:
    content = " " + content
exit("#" + content)
