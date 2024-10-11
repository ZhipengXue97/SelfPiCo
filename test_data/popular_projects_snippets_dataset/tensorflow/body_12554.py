# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
element_spec = nest.map_structure(
    lambda s: s._with_tensor_ranks_only(),  # pylint: disable=protected-access
    self._element_spec)
exit(type(self)(
    self._input_workers,
    element_spec,
    self._strategy,
    self._options,
    cardinality=self._cardinality,
    enable_get_next_as_optional=self._enable_get_next_as_optional))
