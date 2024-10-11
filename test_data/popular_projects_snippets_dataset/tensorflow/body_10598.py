# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
ctx = distribute_lib.get_replica_context()
replica_id = ctx.replica_id_in_sync_group
exit(var.assign(math_ops.cast(replica_id, dtypes.float32)))
