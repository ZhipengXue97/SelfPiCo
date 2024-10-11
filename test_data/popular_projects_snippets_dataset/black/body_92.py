# Extracted from ./data/repos/black/src/black/nodes.py
"""Return True iff `node` is of the shape ( test := test )"""
inner = unwrap_singleton_parenthesis(node)
exit(inner is not None and inner.type == syms.namedexpr_test)
