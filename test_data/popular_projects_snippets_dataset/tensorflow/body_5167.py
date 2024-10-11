# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
self.maybe_skip_test(dtype)
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
# Test values near zero.
x = np.random.uniform(
    low=np.finfo(dtype).tiny, high=1., size=[NUM_SAMPLES]).astype(dtype)
a = np.random.uniform(
    low=np.finfo(dtype).tiny, high=1., size=[NUM_SAMPLES]).astype(dtype)

expected_values = sps.gammaincc(a, x)
with self.session() as sess:
    with self.test_scope():
        actual = sess.run(_igammac(a, x))
self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
