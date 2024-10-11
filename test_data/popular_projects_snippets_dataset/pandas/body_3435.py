# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
lhs = self._try_visit_binop(x)
rhs = self._try_visit_binop(y)

op, op_class, lhs, rhs = self._maybe_transform_eq_ne(node, lhs, rhs)
exit(self._maybe_evaluate_binop(op, node.op, lhs, rhs))
