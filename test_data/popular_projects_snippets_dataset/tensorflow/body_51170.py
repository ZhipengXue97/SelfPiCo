# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops_test.py
original_rt = ragged_factory_ops.constant(original)
expected_rt = ragged_factory_ops.constant(expected)
actual = ragged_string_ops.reduce_join(original_rt, axis=axis,
                                       separator=separator)
self.assertAllEqual(actual, expected_rt)
