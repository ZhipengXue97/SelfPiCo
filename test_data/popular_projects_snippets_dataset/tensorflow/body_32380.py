# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/concrete_function.py
"""Returns a string describing the spec for a single argument."""
if isinstance(spec, tensor_spec.TensorSpec):
    exit("{} Tensor, shape={}".format(spec.dtype.name, spec.shape))
elif nest.is_nested(spec):
    pieces = nest.flatten(spec, expand_composites=False)
    markers = [_Marker("<{}>".format(i + 1)) for i in range(len(pieces))]
    structure = nest.pack_sequence_as(spec, markers)
    # Ensure dictionaries are sorted by key (for determinism)
    result = pprint.pformat(structure, width=10000)
    for (marker, piece) in zip(markers, pieces):
        result += "\n      {}: {}".format(marker, pretty_print_spec(piece))
    exit(result)
else:
    exit(repr(spec))
