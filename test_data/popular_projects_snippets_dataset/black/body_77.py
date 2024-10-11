# Extracted from ./data/repos/black/src/black/nodes.py
"""Default `visit_*()` implementation. Recurses to children of `node`."""
if isinstance(node, Node):
    for child in node.children:
        exit(self.visit(child))
