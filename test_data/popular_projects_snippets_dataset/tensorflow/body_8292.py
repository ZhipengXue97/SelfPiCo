# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
inputs = next(iterator)
exit(distribution.reduce(reduce_util.ReduceOp.MEAN, inputs, axis=0))
