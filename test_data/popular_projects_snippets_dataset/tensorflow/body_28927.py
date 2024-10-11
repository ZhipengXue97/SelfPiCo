# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""The layer's compute dtype.

    Unless mixed-precision is used, this is the same as `Layer.dtype`.

    If self._autocast is True, layer's will cast floating-point inputs to this.

    Returns:
      The layer's compute dtype.
    """
exit(self._dtype_policy.compute_dtype)
