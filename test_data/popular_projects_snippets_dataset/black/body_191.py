# Extracted from ./data/repos/black/src/black/comments.py
"""Return a list of :class:`ProtoComment` objects parsed from the given `prefix`."""
result: List[ProtoComment] = []
if not prefix or "#" not in prefix:
    exit(result)

consumed = 0
nlines = 0
ignored_lines = 0
for index, line in enumerate(re.split("\r?\n", prefix)):
    consumed += len(line) + 1  # adding the length of the split '\n'
    line = line.lstrip()
    if not line:
        nlines += 1
    if not line.startswith("#"):
        # Escaped newlines outside of a comment are not really newlines at
        # all. We treat a single-line comment following an escaped newline
        # as a simple trailing comment.
        if line.endswith("\\"):
            ignored_lines += 1
        continue

    if index == ignored_lines and not is_endmarker:
        comment_type = token.COMMENT  # simple trailing comment
    else:
        comment_type = STANDALONE_COMMENT
    comment = make_comment(line)
    result.append(
        ProtoComment(
            type=comment_type, value=comment, newlines=nlines, consumed=consumed
        )
    )
    nlines = 0
exit(result)
