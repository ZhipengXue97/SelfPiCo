# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
scope = g.device("/device:GPU:8")
scope.__enter__()
with g.device("/device:GPU:9"):
    with self.assertRaises(RuntimeError):
        scope.__exit__(None, None, None)
