# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = dict(a=3, b=[7, 2.5])
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
expected = struct_pb2.StructuredValue()
expected.dict_value.fields["a"].int64_value = 3
list_value = expected.dict_value.fields["b"].list_value
list_value.values.add().int64_value = 7
list_value.values.add().float64_value = 2.5
self.assertEqual(expected, encoded)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertIsInstance(decoded["a"], int)
self.assertEqual(structure, decoded)
