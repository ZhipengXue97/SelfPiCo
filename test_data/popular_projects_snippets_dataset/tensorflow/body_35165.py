# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
np_ans = x
if reduction_axes is None:
    np_ans = np.amax(np_ans, keepdims=keepdims)
else:
    for ra in reduction_axes[::-1]:
        np_ans = np.amax(np_ans, axis=ra, keepdims=keepdims)
with self.cached_session(use_gpu=use_gpu):
    if reduction_axes is not None:
        reduction_axes = np.array(reduction_axes).astype(np.int32)
    tf_ans = math_ops.reduce_max(x, reduction_axes, keepdims)
    out = self.evaluate(tf_ans)
self.assertAllClose(np_ans, out)
self.assertShapeEqual(np_ans, tf_ans)
