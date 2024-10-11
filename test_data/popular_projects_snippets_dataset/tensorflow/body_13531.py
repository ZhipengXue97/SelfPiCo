# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
self._test_restored_func_with_captured_var_backprop(
    cycles, use_cpp_bindings, dtypes.float32
)
