# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that a CPU RNG can split into RNGs on GPU."""
with ops.device("/device:CPU:0"):
    gen = random.Generator.from_seed(1234, alg=alg)  # gen is on CPU
    self.assertRegex("CPU", gen.state.device)
if alg == random_ops_util.Algorithm.THREEFRY:
    # We don't have CPU/GPU kernels for ThreeFry yet.
    exit()
with ops.device(test_util.gpu_device_name()):
    gens = gen.split(count=10)  # gens are on GPU
    self.assertRegex("GPU", gens[0].state.device)
