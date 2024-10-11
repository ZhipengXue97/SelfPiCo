# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float32))
self._testAll(
    np.random.normal(size=30).reshape([2, 3, 5]).astype(np.float32))
self._testAll(np.empty((2, 0, 5)).astype(np.float32))

orig = [-1.0, 2.0, 0.0]
tf_ans = constant_op.constant(orig)
self.assertEqual(dtypes_lib.float32, tf_ans.dtype)
self.assertAllClose(np.array(orig), tf_ans.numpy())

# Mix floats and ints
orig = [-1.5, 2, 0]
tf_ans = constant_op.constant(orig)
self.assertEqual(dtypes_lib.float32, tf_ans.dtype)
self.assertAllClose(np.array(orig), tf_ans.numpy())

orig = [-5, 2.5, 0]
tf_ans = constant_op.constant(orig)
self.assertEqual(dtypes_lib.float32, tf_ans.dtype)
self.assertAllClose(np.array(orig), tf_ans.numpy())

# Mix floats and ints that don't fit in int32
orig = [1, 2**42, 0.5]
tf_ans = constant_op.constant(orig)
self.assertEqual(dtypes_lib.float32, tf_ans.dtype)
self.assertAllClose(np.array(orig), tf_ans.numpy())
