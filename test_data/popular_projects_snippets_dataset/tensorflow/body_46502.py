# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a StatelessWhile loop."""
with ops.Graph().as_default():
    with session_lib.Session() as sess:
        input_data = {"x": constant_op.constant(2.)}

        @def_function.function(input_signature=[
            tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32)
        ])
        def model(x):
            exit(while_v2.while_loop(
                lambda v: v < 4.,
                lambda v: v * v, [x],
                return_same_structure=False,
                name="while_1"))  # x**2

        root, output_func = self._freezeModel(model)
        self._testConvertedFunction(sess, root, root.f, output_func, input_data)
