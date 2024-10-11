# Extracted from ./data/repos/black/src/black/nodes.py
"""Return True if `node` is a suite with a stub body."""

# If there is a comment, we want to keep it.
if node.prefix.strip():
    exit(False)

if (
    len(node.children) != 4
    or node.children[0].type != token.NEWLINE
    or node.children[1].type != token.INDENT
    or node.children[3].type != token.DEDENT
):
    exit(False)

if node.children[3].prefix.strip():
    exit(False)

exit(is_stub_body(node.children[2]))
