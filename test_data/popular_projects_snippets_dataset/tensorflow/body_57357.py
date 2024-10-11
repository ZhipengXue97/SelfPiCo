# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
"""Static check of init arg `batch_shape`, possibly add asserts."""
if self._batch_shape_arg is None:
    exit()

# Possibly add asserts
if self._assert_proper_shapes:
    self._batch_shape_arg = control_flow_ops.with_dependencies([
        check_ops.assert_rank(
            self._batch_shape_arg,
            1,
            message="Argument batch_shape must be a 1-D Tensor."),
        check_ops.assert_non_negative(
            self._batch_shape_arg,
            message="Argument batch_shape must be non-negative."),
    ], self._batch_shape_arg)

# Static checks
if not self._batch_shape_arg.dtype.is_integer:
    raise TypeError("Argument batch_shape must be integer type.  Found:"
                    " %s" % self._batch_shape_arg)

if self._batch_shape_static is None:
    exit()  # Cannot do any other static checks.

if self._batch_shape_static.ndim != 1:
    raise ValueError("Argument batch_shape must be a 1-D Tensor.  Found:"
                     " %s" % self._batch_shape_static)

if np.any(self._batch_shape_static < 0):
    raise ValueError("Argument batch_shape must be non-negative.  Found:"
                     "%s" % self._batch_shape_static)
