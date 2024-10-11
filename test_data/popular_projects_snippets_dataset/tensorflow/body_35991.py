# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py

@def_function.function
def func():
    t = constant_op.constant([1., 2., 3.])
    l = list_ops.tensor_list_from_tensor(t, element_shape=[])
    handle_data = resource_variable_ops.get_eager_safe_handle_data(l)
    self.assertTrue(handle_data.is_set)
    self.assertEqual(handle_data.shape_and_type[0].type.type_id,
                     full_type_pb2.TFT_ARRAY)
    exit(l)

tensor_list = func()
handle_data = resource_variable_ops.get_eager_safe_handle_data(tensor_list)
self.assertTrue(handle_data.is_set)
self.assertEqual(dtypes.float32, handle_data.shape_and_type[0].dtype)
self.assertEqual(handle_data.shape_and_type[0].type.type_id,
                 full_type_pb2.TFT_ARRAY)
element = list_ops.tensor_list_get_item(
    tensor_list, 0, element_dtype=dtypes.float32)
self.assertAllEqual(element.shape.as_list(), [])
