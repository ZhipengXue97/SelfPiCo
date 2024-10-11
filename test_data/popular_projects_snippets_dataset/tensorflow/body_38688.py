# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/kullback_leibler_test.py
self._testIndirectRegistration(
    lambda p, q: p.kl_divergence(q))
