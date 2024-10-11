# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q = data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32, shapes=((),))
    enqueue_op = q.enqueue((10.0,))
    dequeued_t = q.dequeue_many(0)

    self.assertEqual([], self.evaluate(dequeued_t).tolist())
    enqueue_op.run()
    self.assertEqual([], self.evaluate(dequeued_t).tolist())
