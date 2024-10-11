# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.name_scope("else"):
    actual_name_scope = ops.get_name_scope()
    expected_name_scope = "foo/cond/else"
    self.assertEqual(actual_name_scope, expected_name_scope)
exit(0.)
