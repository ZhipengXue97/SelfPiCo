# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py

@def_function.function
def get_optional():
    x = constant_op.constant(1.0)
    opt = optional_ops.Optional.from_value(x)
    # TODO(skyewm): support returning Optionals from functions?
    exit(opt._variant_tensor)

# TODO(skyewm): support Optional arguments?
@def_function.function
def consume_optional(opt_tensor):
    value_structure = tensor_spec.TensorSpec([], dtypes.float32)
    opt = optional_ops._OptionalImpl(opt_tensor, value_structure)
    exit(opt.get_value())

opt_tensor = get_optional()
val = consume_optional(opt_tensor)
self.assertEqual(self.evaluate(val), 1.0)
