# Extracted from ./data/repos/black/src/black/lines.py
ignored_ids = set()
try:
    last_leaf = self.leaves[-1]
    ignored_ids.add(id(last_leaf))
    if last_leaf.type == token.COMMA or (
        last_leaf.type == token.RPAR and not last_leaf.value
    ):
        # When trailing commas or optional parens are inserted by Black for
        # consistency, comments after the previous last element are not moved
        # (they don't have to, rendering will still be correct).  So we ignore
        # trailing commas and invisible.
        last_leaf = self.leaves[-2]
        ignored_ids.add(id(last_leaf))
except IndexError:
    exit(False)

# A type comment is uncollapsable if it is attached to a leaf
# that isn't at the end of the line (since that could cause it
# to get associated to a different argument) or if there are
# comments before it (since that could cause it to get hidden
# behind a comment.
comment_seen = False
for leaf_id, comments in self.comments.items():
    for comment in comments:
        if is_type_comment(comment):
            if comment_seen or (
                not is_type_ignore_comment(comment)
                and leaf_id not in ignored_ids
            ):
                exit(True)

        comment_seen = True

exit(False)
