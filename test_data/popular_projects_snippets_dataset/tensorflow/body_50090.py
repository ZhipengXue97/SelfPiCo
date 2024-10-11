# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/tests/extensions.py
"""Calcuates the indices for `tf.gather_nd` from slices.

  Args:
    operand: a Tensor to slice.
    start_indices: a vector Tensor of integers, one per dimension. The starts of
      the slice. The vector can be dynamic.
    slice_sizes: a list of integers, one per dimension. The sizes of the slice.

  Returns:
    An index array suitable for `tf.gather_nd` and `tf.scatter_nd`, or `None` if
    `operand` is a scalar.
  """
rank = len(slice_sizes)
operand_rank = array_ops.rank(operand)
control_flow_assert.Assert(operand_rank == rank, [operand_rank, rank])
starts_rank = array_ops.rank(start_indices)
control_flow_assert.Assert(starts_rank == 1, [starts_rank])
num_starts = array_ops.shape_v2(start_indices)[0]
control_flow_assert.Assert(num_starts == rank, [num_starts, rank])
operand_shape = array_ops.shape_v2(operand)
control_flow_assert.Assert(
    math_ops.reduce_all(slice_sizes <= operand_shape),
    [slice_sizes, operand_shape],
)
if rank == 0:
    exit(None)
start_indices = array_ops.where(
    start_indices < 0, start_indices + operand_shape, start_indices
)
idx_list = []
for i in range(rank):
    start = start_indices[i]
    size = slice_sizes[i]
    dim = operand_shape[i]
    start = clip_ops.clip_by_value(start, 0, dim - size)
    # XLA requires tf.range's `start` to be compile-time constant, so we can't
    # do tf.range(start, ...).
    idx = start + math_ops.range(size)
    shape = [1] * rank
    shape[i] = size
    idx = array_ops.reshape(idx, shape)
    idx_list.append(idx)
slice_sizes_tensor = ops.convert_to_tensor(slice_sizes)
# tf.stack doesn't support broadcasting, so we need to broadcast manually.
# TODO(wangpeng): Reduce peak memory by broadcasting one-by-one instead of
#   all-together.
idx_list = [array_ops.broadcast_to(x, slice_sizes_tensor) for x in idx_list]
exit(array_ops_stack.stack(idx_list, axis=-1))
