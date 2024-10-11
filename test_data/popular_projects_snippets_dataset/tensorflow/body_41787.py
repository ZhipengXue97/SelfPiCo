# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
np_ans = np.array(np.shape(x))
with self.cached_session(use_gpu=use_gpu):
    tf_ans = array_ops.shape(x)
    tf_ans_64 = array_ops.shape(x, out_type=dtypes.int64)
    result = self.evaluate(tf_ans)
    result_64 = self.evaluate(tf_ans_64)
self.assertAllEqual(np_ans, result)
self.assertAllEqual(np_ans, result_64)
self.assertShapeEqual(np_ans, tf_ans)
