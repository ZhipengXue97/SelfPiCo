# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.use_gpu():
    sp_input = sparse_tensor.SparseTensor(
        indices=np.array([[2, 3], [2, 2], [0, 1], [0, 3]]),
        values=np.array([1, 3, 2, 4]),
        dense_shape=np.array([3, 5]))
    sp_output, empty_row_indicator = (
        sparse_ops.sparse_fill_empty_rows(sp_input, -1))

    output, empty_row_indicator_out = self.evaluate(
        [sp_output, empty_row_indicator])

    self.assertAllEqual(output.indices,
                        [[0, 1], [0, 3], [1, 0], [2, 3], [2, 2]])
    self.assertAllEqual(output.values, [2, 4, -1, 1, 3])
    self.assertAllEqual(output.dense_shape, [3, 5])
    self.assertAllEqual(empty_row_indicator_out, [False, True, False])
