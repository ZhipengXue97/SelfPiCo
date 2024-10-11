# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
with backprop.GradientTape() as tape:
    loss = math_ops.sin(math_ops.square(v))
    gradients = tape.gradient(loss, v)
exit(gradients)
