# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
# Test case for GitHub issue 55263
a = np.empty([6, 0])
b = np.array([1, -1])
with self.assertRaisesRegex(errors.InvalidArgumentError, "must >= 0"):
    with self.session():
        v = fft_ops.rfft2d(input_tensor=a, fft_length=b)
        self.evaluate(v)
