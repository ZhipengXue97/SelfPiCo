# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# MaxPoolWithArgMax is implemented only on CUDA.
if not test.is_gpu_available(cuda_only=True):
    exit()
self._CompareMaxPoolingFwd(input_size, filter_size, strides, padding)
