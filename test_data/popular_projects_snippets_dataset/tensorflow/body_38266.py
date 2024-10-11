# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
for axis in (1, -1):
    sp_tensors_3 = self.evaluate(
        sparse_ops.sparse_split(
            sp_input=self._SparseTensor_5x7(), num_split=3, axis=axis))
    self.assertAllEqual(len(sp_tensors_3), 3)
    self.assertAllEqual(
        sp_tensors_3[0].indices,
        [[0, 0], [0, 2], [1, 1], [2, 0], [3, 0], [3, 2], [4, 1]])
    self.assertAllEqual(sp_tensors_3[0].values, [0, 2, 11, 20, 30, 32, 41])
    self.assertAllEqual(sp_tensors_3[0].dense_shape, [5, 3])
    self.assertAllEqual(sp_tensors_3[1].indices,
                        [[0, 1], [1, 0], [1, 1], [2, 0], [3, 0], [4, 1]])
    self.assertAllEqual(sp_tensors_3[1].values, [4, 13, 14, 23, 33, 44])
    self.assertAllEqual(sp_tensors_3[1].dense_shape, [5, 2])
    self.assertAllEqual(sp_tensors_3[2].indices,
                        [[0, 0], [1, 1], [2, 0], [3, 0], [4, 1]])
    self.assertAllEqual(sp_tensors_3[2].values, [5, 16, 25, 35, 46])
    self.assertAllEqual(sp_tensors_3[2].dense_shape, [5, 2])
    sp_tensors_4 = sparse_ops.sparse_split(
        sp_input=self._SparseTensor_5x7(), num_split=4, axis=axis)
    self.assertAllEqual(len(sp_tensors_4), 4)
    self.assertAllEqual(sp_tensors_4[0].indices,
                        [[0, 0], [1, 1], [2, 0], [3, 0], [4, 1]])
    self.assertAllEqual(sp_tensors_4[0].values, [0, 11, 20, 30, 41])
    self.assertAllEqual(sp_tensors_4[0].dense_shape, [5, 2])
    self.assertAllEqual(sp_tensors_4[1].indices,
                        [[0, 0], [1, 1], [2, 1], [3, 0], [3, 1]])
    self.assertAllEqual(sp_tensors_4[1].values, [2, 13, 23, 32, 33])
    self.assertAllEqual(sp_tensors_4[1].dense_shape, [5, 2])
    self.assertAllEqual(sp_tensors_4[2].indices,
                        [[0, 0], [0, 1], [1, 0], [2, 1], [3, 1], [4, 0]])
    self.assertAllEqual(sp_tensors_4[2].values, [4, 5, 14, 25, 35, 44])
    self.assertAllEqual(sp_tensors_4[2].dense_shape, [5, 2])
    self.assertAllEqual(sp_tensors_4[3].indices, [[1, 0], [4, 0]])
    self.assertAllEqual(sp_tensors_4[3].values, [16, 46])
    self.assertAllEqual(sp_tensors_4[3].dense_shape, [5, 1])
