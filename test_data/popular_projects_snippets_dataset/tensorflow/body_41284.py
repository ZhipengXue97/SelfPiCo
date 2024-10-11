# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
with self.session():
    p1 = array_ops.placeholder(dtypes.float32, shape=[2, 3, 1, 1])
    p2 = array_ops.placeholder(dtypes.float32, shape=[2, 3, 4, 1])
    c = array_ops.concat([p1, p2], 2)
    params = {
        p1: np.random.rand(2, 3, 1, 1).astype("f"),
        p2: np.random.rand(2, 3, 4, 1).astype("f")
    }
    result = c.eval(feed_dict=params)

self.assertEqual(result.shape, c.get_shape())
self.assertAllEqual(result[:, :, :1, :], params[p1])
self.assertAllEqual(result[:, :, 1:, :], params[p2])
