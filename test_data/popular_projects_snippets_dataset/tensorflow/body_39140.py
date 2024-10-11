# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mel_ops_test.py
# LinSpace is not supported for tf.float16.
self.assertEqual(dtype,
                 mel_ops.linear_to_mel_weight_matrix(dtype=dtype).dtype)
