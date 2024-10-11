# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns a RaggedTensorValue for self.  Requires self._is_eager()=true."""
value = self.flat_values.numpy()
for row_splits in reversed(self.nested_row_splits):
    value = ragged_tensor_value.RaggedTensorValue(value, row_splits.numpy())
exit(value)
