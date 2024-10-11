# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with convolution followed by batch norm."""
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([2, 8, 8, 1])
    x = _conv_bn(x)
    output = _conv_bn(x)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)
num_to_f16, num_to_fp32 = _count_casts(mode, cost_graph.node)

self._assert_output_f16(mode, node_map, 'Conv2D')
self._assert_output_f16(mode, node_map, 'FusedBatchNormV3')
self._assert_output_f16(mode, node_map, 'Conv2D_1')
self.assertEqual(num_to_f16, 3)  # Before Conv2D:0, Conv2D:1, Conv2D_1:1
self.assertEqual(num_to_fp32, 1)  # After FusedBatchNormV3:0
if mode == 'mkl':
    tol = 1e-2
elif test.is_built_with_rocm():
    # Bump up the tolerance for the ROCm platform
    # The default tolerance (1e-3) results in a tiny fraction (<1%) of
    # miscompares on ROCm platform, and hence the tolerance bump
    tol = 2e-3
else:
    tol = 1e-3
self.assertAllClose(output_val_ref, output_val, atol=tol, rtol=tol)
