# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tensor = constant_op.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
begins = constant_op.constant([0, 0], dtype=dtypes.int32)

@polymorphic_function.function
def slice_fn(tensor, begins):
    exit(array_ops.slice(tensor, begins, [2, 2]))

expected_result = slice_fn(tensor, begins)

sharded_layout = self.first_dimension_sharded_layout

tensor = api.relayout(tensor, sharded_layout)
begins = api.relayout(begins, self.replicated_layout_1d)

dtensor_result = slice_fn(tensor, begins)

self.assertDTensorEqual(expected_result, sharded_layout, dtensor_result)
