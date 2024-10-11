# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
input_data = ragged_factory_ops.constant([[0, 1, 2, 3], [], [4], []])
actual = input_data.to_tensor(
    shape=constant_op.constant([2, 3], dtype=dtypes.int64))
self.assertAllEqual(actual, [[0, 1, 2], [0, 0, 0]])
self.assertEqual(actual.shape.as_list(), [2, 3])
