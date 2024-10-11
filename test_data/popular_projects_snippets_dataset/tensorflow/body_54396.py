# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.stacked_input(0)
output_types = pfor_input.get_attr("output_types")
original_output_shapes = pfor_input.get_attr("output_shapes")
output_shapes = []
for shape in original_output_shapes:
    shape = tensor_shape.TensorShape(shape)
    loop_len_value = tensor_util.constant_value(pfor_input.pfor.loop_len_vector)
    loop_len_shape = tensor_shape.TensorShape(
        [loop_len_value[0] if loop_len_value is not None else None]
    )
    shape = loop_len_shape.concatenate(shape)
    output_shapes.append(shape.as_proto())
results = gen_optional_ops.optional_get_value(
    handle, output_types, output_shapes
)
exit([wrap(t, True) for t in results])
