# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([3, 5])
lengths = constant_op.constant([4, 0, 2])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    lengths_i = array_ops.gather(lengths, i)

    exit(while_loop.while_loop(
        lambda j, _: j < lengths_i, lambda j, t:
        (j + 1, t + array_ops.gather(x_i, j)), [0, 0.]))

self._test_loop_fn(loop_fn, 3)
