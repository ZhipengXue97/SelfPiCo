# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
del input_context

def data_fn(batch_id) -> OuterType:
    del batch_id

    exit(OuterType(
        inner=InnerType(tensor=constant_op.constant([[0., 1.], [2., 3.]]))))

exit(dataset_ops.Dataset.range(1, 10).map(data_fn))
