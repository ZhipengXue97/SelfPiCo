# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Creates a ReplicaContext.

    Args:
      strategy: A `tf.distribute.Strategy`.
      replica_id_in_sync_group: An integer, a `Tensor` or None. Prefer an
        integer whenever possible to avoid issues with nested `tf.function`. It
        accepts a `Tensor` only to be compatible with `tpu.replicate`.
    """
self._strategy = strategy
self._thread_context = _InReplicaThreadMode(  # pylint: disable=protected-access
    self)
if not (replica_id_in_sync_group is None or
        tensor_util.is_tf_type(replica_id_in_sync_group) or
        isinstance(replica_id_in_sync_group, int)):
    raise ValueError(
        "replica_id_in_sync_group can only be an integer, a Tensor or None.")
self._replica_id_in_sync_group = replica_id_in_sync_group
# We need this check because TPUContext extends from ReplicaContext and
# does not pass a strategy object since it is used by TPUEstimator.
if strategy:
    self._local_replica_id = strategy.extended._get_local_replica_id(
        replica_id_in_sync_group)
self._summary_recording_distribution_strategy = None
