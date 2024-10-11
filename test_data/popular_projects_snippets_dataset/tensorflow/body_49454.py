# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
ctx = tf.distribute.get_replica_context()
val = np.asarray(ctx.replica_id_in_sync_group)
exit(val * multiplier)
