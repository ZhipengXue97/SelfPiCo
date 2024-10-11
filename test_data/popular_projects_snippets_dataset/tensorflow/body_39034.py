# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = array_ops.placeholder(np.int32, shape=None)
shape = du.prefer_static_shape(x)
with self.cached_session():
    self.assertAllEqual(np.array([]), shape.eval(feed_dict={x: 1}))
