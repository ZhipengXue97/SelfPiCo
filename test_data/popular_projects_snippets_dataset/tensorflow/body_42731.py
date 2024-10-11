# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/dense_update_ops_no_tsan_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    zeros_t = array_ops.fill([1024, 1024], 0.0)
    ones_t = array_ops.fill([1024, 1024], 1.0)
    p = variables.Variable(zeros_t)
    adds = [
        state_ops.assign_add(
            p, ones_t, use_locking=True) for _ in range(20)
    ]
    self.evaluate(p.initializer)

    def run_add(add_op):
        self.evaluate(add_op)

    threads = [
        self.checkedThread(
            target=run_add, args=(add_op,)) for add_op in adds
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    vals = self.evaluate(p)
    ones = np.ones((1024, 1024)).astype(np.float32)
    self.assertAllEqual(vals, ones * 20)
