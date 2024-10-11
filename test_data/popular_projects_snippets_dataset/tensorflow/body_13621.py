# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
v1 = variables.Variable(1.0)
weak_v1 = weakref.ref(v1)
root = checkpoint.Checkpoint(v=v1)
root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
del v1
self.assertIsNone(weak_v1())
weak_v2 = weakref.ref(root.v)
del root
self.assertIsNone(weak_v2())
