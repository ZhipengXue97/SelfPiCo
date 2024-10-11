# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
default = ops.Tensor._USE_EQUALITY

try:
    def _v1_check(a, b):
        self.assertEqual(a, a)
        self.assertIs(a, a)
        self.assertNotEqual(a, float('nan'))
        self.assertIsNot(a, float('nan'))
        self.assertNotEqual(a, b)
        self.assertIsNot(a, b)

    def _v2_check(a, b):
        self.assertNotEqual(a, a)
        self.assertIs(a, a)
        self.assertNotEqual(a, float('nan'))
        self.assertIsNot(a, float('nan'))
        self.assertNotEqual(a, b)
        self.assertIsNot(a, b)

    constant_a = constant_op.constant(float('nan'))
    constant_b = constant_op.constant(float('nan'))

    ops.disable_tensor_equality()
    self._test_hashable(constant_a, constant_b, False)
    _v1_check(constant_a, constant_b)
    ops.enable_tensor_equality()
    _v2_check(constant_a, constant_b)
    self._test_hashable(constant_a, constant_b, False)

    variable_a = variables.Variable(float('nan'))
    variable_b = variables.Variable(float('nan'))

    ops.disable_tensor_equality()
    _v1_check(variable_a, variable_b)
    self._test_hashable(variable_a, variable_b, True)
    ops.enable_tensor_equality()
    _v2_check(variable_a, variable_b)
    self._test_hashable(variable_a, variable_b, False)

    numpy_a = np.array(float('nan'))
    numpy_b = np.array(float('nan'))
    _v2_check(numpy_a, numpy_b)
    self._test_hashable(numpy_a, numpy_b, False)
finally:
    if default:
        ops.enable_tensor_equality()
    else:
        ops.disable_tensor_equality()
