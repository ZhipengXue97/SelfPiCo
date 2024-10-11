# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Indicates whether two type specifications are compatible.

  Two type specifications are compatible if they have the same nested structure
  and the their individual components are pair-wise compatible.

  Args:
    spec1: A `tf.TypeSpec` object to compare.
    spec2: A `tf.TypeSpec` object to compare.

  Returns:
    `True` if the two type specifications are compatible and `False` otherwise.
  """

try:
    nest.assert_same_structure(spec1, spec2)
except TypeError:
    exit(False)
except ValueError:
    exit(False)

for s1, s2 in zip(nest.flatten(spec1), nest.flatten(spec2)):
    if not s1.is_compatible_with(s2) or not s2.is_compatible_with(s1):
        exit(False)
exit(True)
