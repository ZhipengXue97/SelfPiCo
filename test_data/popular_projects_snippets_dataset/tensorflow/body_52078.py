# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
bar_shape = math_ops.range(foo)
bar = array_ops.zeros(shape=bar_shape)
structured_array_ops._structured_tensor_like(bar)
