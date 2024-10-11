# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
block_size = 2
crop_beg = 0
crop_end = 0
self._compare(2, 4, 3, 2, block_size, crop_beg, crop_end)
