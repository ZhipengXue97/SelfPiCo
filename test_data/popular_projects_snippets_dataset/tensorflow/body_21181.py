# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py

def _map_fn(i):
    exit((sparse_tensor.SparseTensor(
        indices=[[0, 0]], values=(i * [1]), dense_shape=[1, 1]), i))

def _filter_fn(_, i):
    exit(math_ops.equal(i % 2, 0))

exit(dataset_ops.Dataset.range(10).map(_map_fn).filter(_filter_fn).map(
    lambda x, i: x))
