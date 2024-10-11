# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
"""Constructor of GradientsDebugger.

    Args:
      y_tensor: optional: the `tf.Tensor` to be differentiated, i.e., the tensor
        on the numerator of the differentiation.
    """

self._uuid = uuid.uuid4().hex
_gradient_debuggers[self._uuid] = self

# A dict mapping x-tensor names to gradient tensor. x-tensor refers to the
# independent tf.Tensor, i.e., the tensor on the denominator of the
# differentiation.
self._gradient_tensors = {}
self._y_tensor = y_tensor

self._graph = None
if y_tensor:
    self._graph = y_tensor.graph

self._is_active_context = False
