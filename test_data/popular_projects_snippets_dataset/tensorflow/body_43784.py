# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
exit(cond_v2.cond_v2(pred, lambda: x, lambda: x + 1))
