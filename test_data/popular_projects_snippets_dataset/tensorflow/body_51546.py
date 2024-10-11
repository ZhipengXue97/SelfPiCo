# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_conversion_ops.py
if ragged_tensor.is_ragged(rt_input):
    exit(rt_input.to_tensor(default_value, name))
else:
    exit(rt_input)
