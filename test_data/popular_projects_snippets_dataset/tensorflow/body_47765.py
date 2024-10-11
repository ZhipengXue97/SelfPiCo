# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = constant_op.constant([0, 1, 2])
y = constant_op.constant([1, 1, 1])

z = x | y

self.assertAllEqual(z, [1, 1, 3])
