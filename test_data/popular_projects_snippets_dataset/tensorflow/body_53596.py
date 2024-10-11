# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    x = constant_op.constant([[[-3, 5], [7, 11]], [[13, 17], [19, 23]]],
                             dtype=dtype)
    grads = gradient_checker_v2.compute_gradient(
        lambda x: math_ops.reduce_euclidean_norm(x, 2), [x])
    err = gradient_checker_v2.max_error(*grads)
    self.assertLess(err, 2e-3)
