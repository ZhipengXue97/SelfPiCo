# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = np.random.rand(3)
b = np.random.rand(3)
dist = beta_lib.Beta(a, b)
self.assertAllEqual([], self.evaluate(dist.event_shape_tensor()))
self.assertAllEqual([3], self.evaluate(dist.batch_shape_tensor()))
self.assertEqual(tensor_shape.TensorShape([]), dist.event_shape)
self.assertEqual(tensor_shape.TensorShape([3]), dist.batch_shape)
