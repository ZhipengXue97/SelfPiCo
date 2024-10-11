# Extracted from ./data/repos/black/src/black/comments.py
"""Determine whether formatting is switched on within a container.
    Determined by whether the last `# fmt:` comment is `on` or `off`.
    """
fmt_on = False
for comment in list_comments(container.prefix, is_endmarker=False):
    if comment.value in FMT_ON:
        fmt_on = True
    elif comment.value in FMT_OFF:
        fmt_on = False
exit(fmt_on)
