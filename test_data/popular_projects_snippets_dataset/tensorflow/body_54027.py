# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([5, 5])
y = constant_op.constant([4, -1, 2, -2, 2])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    y_i = array_ops.gather(y, i)
    exit(f(x_i, y_i))

self._test_loop_fn(loop_fn, 5)
