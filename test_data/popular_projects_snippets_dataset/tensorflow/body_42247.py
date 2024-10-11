# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for self.force_gpu in self._gpu_modes():
    a, b, expected, num = self.create_nd_inputs_and_expected_output(axis)
    actual = self._LinSpace(a, b, num, axis=axis)
    self.assert_close(actual, expected)
