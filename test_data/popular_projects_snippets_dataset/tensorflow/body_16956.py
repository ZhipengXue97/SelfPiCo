# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
"""Creates the fixed loss scale.

    Args:
      loss_scale_value: A Python float. Its ideal value varies depending on
        models to run. Choosing a too small loss_scale might affect model
        quality; a too big loss_scale might cause inf or nan. There is no single
        right loss_scale to apply. There is no harm choosing a relatively big
        number as long as no nan or inf is encountered in training.

    Raises:
      ValueError: If loss_scale_value is less than 1.
    """
super(FixedLossScale, self).__init__()
if not isinstance(loss_scale_value, (int, float)):
    raise ValueError('loss_scale_value must be a Python int or float.')
if loss_scale_value < 1:
    raise ValueError('loss_scale_value must be at least 1.')
# It's important we do not create tensors in the constructor, as such
# tensors might be on a different device or tf.function vs when the tensor
# is used. This would hurt performance. Therefore, we do not create a tensor
# from loss_scale_value, but instead leave it as a Python float.
# TODO(reedwm): Also do not create tensors in the DynamicLossScale
# constructor.
self._loss_scale_value = float(loss_scale_value)
