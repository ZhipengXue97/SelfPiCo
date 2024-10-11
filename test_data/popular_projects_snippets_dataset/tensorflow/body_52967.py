# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Replaces the gradient components in `value` with `component_grads`.

    The gradient of a ResourceVariable is either None or a Tensor. So we don't
    need `value`'s TypeSpec or non-gradient components in this method.

    Args:
      value: A `ResourceVariable` with its gradient components compatible with
        `component_grads`.
      component_grads: A `Tensor` or None as the gradient result.

    Returns:
      The `component_grads`, which is either a `Tensor` or None.
    """
exit(component_grads)
