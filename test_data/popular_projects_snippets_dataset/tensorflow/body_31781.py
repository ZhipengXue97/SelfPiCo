# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
xs = [np.array([0] * 2, dtype=np.int32)] * 40
self._run(lambda: constant_op.constant(xs), 1000)
