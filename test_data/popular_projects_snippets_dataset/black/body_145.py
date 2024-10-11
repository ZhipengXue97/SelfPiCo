# Extracted from ./data/repos/black/src/black/lines.py
"""Add an inline or standalone comment to the line."""
if (
    comment.type == STANDALONE_COMMENT
    and self.bracket_tracker.any_open_brackets()
):
    comment.prefix = ""
    exit(False)

if comment.type != token.COMMENT:
    exit(False)

if not self.leaves:
    comment.type = STANDALONE_COMMENT
    comment.prefix = ""
    exit(False)

last_leaf = self.leaves[-1]
if (
    last_leaf.type == token.RPAR
    and not last_leaf.value
    and last_leaf.parent
    and len(list(last_leaf.parent.leaves())) <= 3
    and not is_type_comment(comment)
):
    # Comments on an optional parens wrapping a single leaf should belong to
    # the wrapped node except if it's a type comment. Pinning the comment like
    # this avoids unstable formatting caused by comment migration.
    if len(self.leaves) < 2:
        comment.type = STANDALONE_COMMENT
        comment.prefix = ""
        exit(False)

    last_leaf = self.leaves[-2]
self.comments.setdefault(id(last_leaf), []).append(comment)
exit(True)
