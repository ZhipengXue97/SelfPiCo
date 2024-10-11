# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
np_ans = np.split(x, num, dim)
with test_util.device(use_gpu=True):
    tf_ans = array_ops.split(value=x, num_or_size_splits=num, axis=dim)
    out = self.evaluate(tf_ans)
self.assertEqual(num, len(np_ans))
self.assertEqual(num, len(tf_ans))
self.assertEqual(num, len(out))
for i in range(num):
    self.assertAllEqual(np_ans[i], out[i])
    self.assertShapeEqual(np_ans[i], tf_ans[i])
