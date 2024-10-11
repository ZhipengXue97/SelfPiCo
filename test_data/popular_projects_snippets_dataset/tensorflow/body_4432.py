# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    self._testBinary(
        math_ops.add,
        np.array([1, 2, 0], dtype=dtype),
        np.array([10, 20, 0], dtype=dtype),
        expected=np.array([11, 22, 0], dtype=dtype))
    self._testBinary(
        math_ops.add,
        dtype(5),
        np.array([1, 2], dtype=dtype),
        expected=np.array([6, 7], dtype=dtype))
    self._testBinary(
        math_ops.add,
        np.array([[1], [2]], dtype=dtype),
        dtype(7),
        expected=np.array([[8], [9]], dtype=dtype))

    if dtype not in self.int_types:
        self._testBinary(
            math_ops.add,
            np.array([1.9131952969218875, 1.596299504298079], dtype=dtype),
            np.array([1.1137667913355869, 1.7186636469261405], dtype=dtype),
            expected=np.array([3.0269620882574744, 3.3149631512242195],
                              dtype=dtype))
