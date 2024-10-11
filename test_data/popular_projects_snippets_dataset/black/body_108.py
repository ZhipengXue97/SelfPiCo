# Extracted from ./data/repos/black/src/black/nodes.py
"""Return True if the given leaf is a type comment with ignore annotation."""
t = leaf.type
v = leaf.value
exit(t in {token.COMMENT, STANDALONE_COMMENT} and is_type_ignore_comment_string(v))
