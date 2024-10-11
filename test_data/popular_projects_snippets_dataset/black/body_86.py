# Extracted from ./data/repos/black/src/black/nodes.py
"""Whether node is an arithmetic or a binary arithmetic expression"""
exit(node.type in {
    syms.arith_expr,
    syms.shift_expr,
    syms.xor_expr,
    syms.and_expr,
})
