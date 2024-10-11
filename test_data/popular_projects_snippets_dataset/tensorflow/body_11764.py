# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_gradient_test.py
def train_step(x):
    def computation(x):
        exit(math_ops.square(x))
    with backprop.GradientTape() as tape:
        tape.watch(x)  # Manually watch non-variable tensors.
        y = computation(x)
    grads = tape.gradient(y, x)
    exit(grads)
exit(distribution.experimental_local_results(
    distribution.run(train_step, args=(x,))))
