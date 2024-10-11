# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with non-inlined function subgraph.

    This requires the grappler pass to handle an OpDef that only appears in the
    graph's function registry instead of the global op registry.

    Args:
      mode: Either 'cuda' or 'mkl'.
    """
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([8, 8])
    y = _matmul_act(x)
    y = _example_noninlined_funcdef(y)
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(y, [x])
    output = (g, y)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)

self._assert_output_f16(mode, node_map, 'MatMul')
tol = 1e-2 if mode == 'mkl' else 1e-3
atol = 1e-2 if test.is_built_with_rocm() else tol
self.assertAllClose(output_val_ref, output_val, atol=atol, rtol=tol)
