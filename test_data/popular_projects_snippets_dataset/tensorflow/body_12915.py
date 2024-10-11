# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {
    "chief": ["127.0.0.1:1234"],
    "ps": ["127.0.0.1:1926", "127.0.0.1:3141"]
}
# A "ps" job shouldn't call this method.
with self.assertRaisesRegex(ValueError, "Unexpected `task_type` 'ps'"):
    multi_worker_util.worker_count(cluster_spec, task_type="ps")
