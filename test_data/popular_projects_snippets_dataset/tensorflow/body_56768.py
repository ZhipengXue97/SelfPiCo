# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
x = op.inputs[0]
y = op.inputs[1]
zeros = array_ops.zeros_like(grad)
xmask = selector_op(x, y)
xgrad = array_ops.where_v2(xmask, grad, zeros)
ygrad = None  # Return None for ygrad since the config allows that.
exit((xgrad, ygrad))
