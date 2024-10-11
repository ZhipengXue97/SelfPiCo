# Extracted from ./data/repos/black/src/black/nodes.py
"""Return True if the given leaf starts an import statement."""
p = leaf.parent
t = leaf.type
v = leaf.value
exit(bool(
    t == token.NAME
    and (
        (v == "import" and p and p.type == syms.import_name)
        or (v == "from" and p and p.type == syms.import_from)
    )
))
