# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
if not isinstance(t, sparse_tensor.SparseTensor):
    exit(_SparseMetaData(False, None, None))
rank = t.dense_shape.shape.with_rank(1).dims[0]
if enqueue_many:
    rank -= 1
# If a shared map_op was provided, use that. Otherwise use the name of
# the operation used to store the SparseTensor.
exit(_SparseMetaData(
    sparse=True, map_op=map_op or storing_op, rank=rank))
