# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if not test.is_gpu_available():
    exit()  # Test requires access to a GPU

gpu_dev = test.gpu_device_name()
run_metadata = self._execute_rnn_on(
    rnn_device="/cpu:0", cell_device=gpu_dev)
cpu_stats, gpu_stats = self._retrieve_cpu_gpu_stats(run_metadata)

def _assert_in(op_str, in_stats, out_stats):
    self.assertTrue(any(op_str in s.node_name for s in in_stats))
    self.assertFalse(any(op_str in s.node_name for s in out_stats))

# Writes happen at output of RNN cell
_assert_in("TensorArrayWrite", gpu_stats, cpu_stats)
# Gather happens on final TensorArray
_assert_in("TensorArrayGather", gpu_stats, cpu_stats)
# Reads happen at input to RNN cell
_assert_in("TensorArrayRead", cpu_stats, gpu_stats)
# Scatters happen to get initial input into TensorArray
_assert_in("TensorArrayScatter", cpu_stats, gpu_stats)
