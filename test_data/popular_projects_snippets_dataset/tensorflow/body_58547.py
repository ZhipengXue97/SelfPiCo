# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for unpack op."""
exit(array_ops_stack.stack(grads, axis=op.get_attr("axis")))
