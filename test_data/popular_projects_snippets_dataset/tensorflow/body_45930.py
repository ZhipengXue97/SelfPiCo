# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/immutable_dict_test.py
d = immutable_dict.ImmutableDict({'x': 1, 'y': 2})
with self.assertRaises(TypeError):
    d['x'] = 5  # pylint: disable=unsupported-assignment-operation
with self.assertRaises(TypeError):
    d['z'] = 5  # pylint: disable=unsupported-assignment-operation
