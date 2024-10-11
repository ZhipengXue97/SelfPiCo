# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        ragged_string_ops.unicode_encode(72, "UTF-8")
with self.cached_session():
    with self.assertRaises(ValueError):
        ragged_string_ops.unicode_encode(constant_op.constant(72), "UTF-8")
