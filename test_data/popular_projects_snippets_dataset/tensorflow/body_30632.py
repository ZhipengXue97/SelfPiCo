# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
super(Pooling3D, self).__init__(name=name, **kwargs)
if data_format is None:
    data_format = backend.image_data_format()
if strides is None:
    strides = pool_size
self.pool_function = pool_function
self.pool_size = conv_utils.normalize_tuple(pool_size, 3, 'pool_size')
self.strides = conv_utils.normalize_tuple(strides, 3, 'strides')
self.padding = conv_utils.normalize_padding(padding)
self.data_format = conv_utils.normalize_data_format(data_format)
self.input_spec = InputSpec(ndim=5)
