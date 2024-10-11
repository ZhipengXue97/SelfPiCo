# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
x.assign_add(3.)

def gradient_func(*grad):
    exit(2. * grad[0])

exit((x, gradient_func))
