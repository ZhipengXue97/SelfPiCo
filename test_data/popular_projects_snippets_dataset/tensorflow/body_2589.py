# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test converting with trackable objects."""
root = self._getMultiFunctionModel()
input_data = tf.constant(1., shape=[1])
add_func = root.add.get_concrete_function(input_data)

converter = lite.TFLiteConverterV2.from_concrete_functions(
    [add_func], trackable_obj=root)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = add_func(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertEqual(expected_value.numpy(), actual_value)
