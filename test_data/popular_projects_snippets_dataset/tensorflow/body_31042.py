# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
x = constant_op.constant([1.])

with forwardprop.ForwardAccumulator(x, constant_op.constant([3.])) as acc:
    y = array_ops.gather(x, 0)
self.assertAllClose(3., acc.jvp(y))
