# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Unpacks a DTensor handle on this DTensor device.

    Packing and unpacking are inverse operations:

    ```
    * unpack(pack(tensors)) == tensors
    * pack(unpack(dtensor)) == dtensor
    ```

    Refer to `dtensor.unpack` for more information.

    Args:
      dtensor: The DTensor to unpack.

    Returns:
      The raw underlying tensor components of the DTensor.

    Raises:
      RuntimeError: When not called eagerly.
    """
if not context.executing_eagerly():
    raise RuntimeError("`unpack` must be called eagerly.")
try:
    tensors = _pywrap_dtensor_device.Unpack(
        context.context()._handle,  # pylint: disable=protected-access
        dtensor,
        self._device_info)
except core._NotOkStatusException as e:  # pylint: disable=protected-access
    raise core._status_to_exception(e) from None  # pylint: disable=protected-access

is_sparse = _pywrap_dtensor_device.IsSparseDTensor(
    context.context()._handle,  # pylint: disable=protected-access.
    dtensor,
    self._device_info)
if is_sparse:
    result = []
    for i in range(len(tensors) // 3):
        result.append(
            sparse_tensor.SparseTensor(tensors[i],
                                       tensors[i + len(tensors) // 3],
                                       tensors[i + 2 * len(tensors) // 3]))
    exit(result)
else:
    exit(tensors)
