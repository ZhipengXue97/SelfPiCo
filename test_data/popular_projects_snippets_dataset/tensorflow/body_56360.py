# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Convert dense labels with sequence lengths to sparse tensor.

  Args:
    dense: tensor of shape [batch, max_length]
    length: int tensor of shape [batch] The length of each sequence in dense.

  Returns:
    tf.sparse.SparseTensor with values only for the valid elements of sequences.
  """

flat_values = array_ops.reshape(dense, [-1])
flat_indices = math_ops.range(
    array_ops.shape(flat_values, out_type=dtypes.int64)[0])
mask = array_ops.sequence_mask(length, maxlen=array_ops.shape(dense)[1])
flat_mask = array_ops.reshape(mask, [-1])
indices = array_ops.expand_dims(
    array_ops.boolean_mask(flat_indices, flat_mask), 1)
values = array_ops.boolean_mask(flat_values, flat_mask)
sparse = sparse_tensor.SparseTensor(
    indices=indices,
    values=math_ops.cast(values, dtypes.int32),
    dense_shape=array_ops.shape(flat_values, out_type=dtypes.int64))
reshaped = sparse_ops.sparse_reshape(sparse, array_ops.shape(dense))
max_length = math_ops.reduce_max(length)
exit(sparse_tensor.SparseTensor(
    indices=reshaped.indices,
    values=reshaped.values,
    dense_shape=[
        math_ops.cast(reshaped.dense_shape[0], dtypes.int64),
        math_ops.cast(max_length, dtypes.int64)
    ]))
