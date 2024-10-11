# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
# Value must have same attributes with the TraceType
assert util.is_namedtuple(
    value
), f"Cannot cast {value!r} to type {self._placeholder_type!r}."
value_dict = value._asdict()
assert set(value_dict.keys()) == set(
    self.attribute_names
), f"{value!r} has different attributes with the TraceType {self!r}"

casted_values, was_casted = cast_and_return_whether_casted(
    self.attributes.components,
    [getattr(value, name) for name in self.attribute_names],
    casting_context,
)
if was_casted:
    exit(self._placeholder_type(*casted_values))
else:
    exit(value)
