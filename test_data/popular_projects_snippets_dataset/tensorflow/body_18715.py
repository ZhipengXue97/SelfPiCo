# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
"""Creates a tf.data service test cluster.

    Args:
      num_workers: The number of workers to initially add to the cluster.
      dispatcher_port: The port to use for the dispatcher.
      work_dir: The work directory to use for the dispatcher. If set to
        `TMP_WORK_DIR`, the cluster will create a new temporary directory to use
        as the work directory. If set to `NO_WORK_DIR`, no work directory will
        be used.
      fault_tolerant_mode: Whether the dispatcher should write its state to a
        journal so that it can recover from restarts.
      job_gc_check_interval_ms: How often the dispatcher should scan through to
        delete old and unused jobs, in milliseconds.
      job_gc_timeout_ms: How long a job needs to be unused before it becomes a
        candidate for garbage collection, in milliseconds.
      worker_timeout_ms: How long to wait for a worker to heartbeat before
        considering it missing, in milliseconds.
      worker_shutdown_quiet_period_ms: When shutting down a worker, how long to
        wait for the gRPC server to process the final requests.
      snapshot_max_chunk_size_bytes: The maximum size of a distributed snapshot
        chunk file.
      worker_max_concurrent_snapshots: The maximum number of snapshots a worker
        can concurrently process.
      start: Whether to immediately start the servers in the cluster. If
        `False`, the servers can be started later by calling
        `start_dispatcher()` and `start_workers()`.
      protocol: The protocol to use for communicating with the tf.data service,
        e.g. "grpc".
      data_transfer_protocol: (Optional.) The protocol to use for transferring
        data with the tf.data service.
    """
if work_dir == TMP_WORK_DIR:
    work_dir = tempfile.mkdtemp(dir=googletest.GetTempDir())
self._worker_shutdown_quiet_period_ms = worker_shutdown_quiet_period_ms
self._snapshot_max_chunk_size_bytes = snapshot_max_chunk_size_bytes
self._protocol = protocol
self._data_transfer_protocol = data_transfer_protocol
self._job_gc_check_interval_ms = job_gc_check_interval_ms
self._job_gc_timeout_ms = job_gc_timeout_ms
self._worker_timeout_ms = worker_timeout_ms
self._worker_max_concurrent_snapshots = worker_max_concurrent_snapshots
self.dispatcher = server_lib.DispatchServer(
    server_lib.DispatcherConfig(
        port=dispatcher_port,
        work_dir=work_dir,
        protocol=protocol,
        fault_tolerant_mode=fault_tolerant_mode,
        job_gc_check_interval_ms=job_gc_check_interval_ms,
        job_gc_timeout_ms=job_gc_timeout_ms,
        worker_timeout_ms=worker_timeout_ms,
        worker_max_concurrent_snapshots=worker_max_concurrent_snapshots,
    ),
    start=start,
)

self.workers = []
for _ in range(num_workers):
    self.add_worker(start=start)
