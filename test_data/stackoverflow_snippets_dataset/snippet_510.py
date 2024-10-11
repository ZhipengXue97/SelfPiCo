# Extracted from https://stackoverflow.com/questions/1305532/how-to-convert-a-nested-python-dict-to-object
from mock import Mock
d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
my_data = Mock(**d)

# We got
# my_data.a == 1

