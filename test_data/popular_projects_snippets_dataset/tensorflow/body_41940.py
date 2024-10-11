# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
"""Test shape inference."""
x = np.arange(6).reshape(3, 2, 1)
_, idx = gen_array_ops.unique_v2(x, axis=[0])
self.assertEqual(idx.shape.as_list(), [3])
_, idx = gen_array_ops.unique_v2(x, axis=[1])
self.assertEqual(idx.shape.as_list(), [2])
_, idx = gen_array_ops.unique_v2(x, axis=[2])
self.assertEqual(idx.shape.as_list(), [1])
_, idx = gen_array_ops.unique_v2(x, axis=[-1])
self.assertEqual(idx.shape.as_list(), [1])
_, idx = gen_array_ops.unique_v2(x, axis=[-2])
self.assertEqual(idx.shape.as_list(), [2])
_, idx = gen_array_ops.unique_v2(x, axis=[-3])
self.assertEqual(idx.shape.as_list(), [3])
_, idx = gen_array_ops.unique_v2([0, 1, 2], axis=[])
self.assertEqual(idx.shape.as_list(), [3])

with self.assertRaisesRegexp(ValueError, "axis expects a 1D vector"):
    gen_array_ops.unique_v2(x, axis=[[0]])

with self.assertRaisesRegexp(ValueError, "x expects a 1D vector"):
    gen_array_ops.unique_v2(x, axis=[])

with self.assertRaisesRegexp(
    ValueError, "axis does not support input tensors larger than"):
    gen_array_ops.unique_v2(x, axis=[1, 2])

with self.assertRaisesRegexp(ValueError,
                             r"axis expects to be in the range \[-3, 3\)"):
    gen_array_ops.unique_v2(x, axis=[3])

with self.assertRaisesRegexp(ValueError,
                             r"axis expects to be in the range \[-3, 3\)"):
    gen_array_ops.unique_v2(x, axis=[-4])

x_t = array_ops.placeholder(dtypes.int32, shape=None)
_, idx = gen_array_ops.unique_v2(x_t, axis=[0])
self.assertEqual(idx.shape.as_list(), [None])

axis_t = array_ops.placeholder(dtypes.int32, shape=None)
_, idx = gen_array_ops.unique_v2(x, axis=axis_t)
self.assertEqual(idx.shape.as_list(), [None])
