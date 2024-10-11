# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV1([1, 2, 3, 4], [True, False, True, False])
y = MaskedTensorV1([5, 6, 7, 8], [False, True, True, False])

x_2 = tf_cond.cond(constant_op.constant(True), lambda: x, lambda: y)
y_2 = tf_cond.cond(constant_op.constant(False), lambda: x, lambda: y)

self.assertAllEqual(x.values, x_2.values)
self.assertAllEqual(x.mask, x_2.mask)
self.assertAllEqual(y.values, y_2.values)
self.assertAllEqual(y.mask, y_2.mask)
