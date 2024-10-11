# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# This test is predicated on the fact that broadcast_to is correct.
# Thus, it tests:
# Whether the shape generated is correct.
# Whether broadcasting is the same as broadcast_to.
# Instead of specifying values, it just uses primes.
shape_a = DynamicRaggedShape.from_lengths(lengths_a)
if num_row_partitions_a is not None:
    shape_a = shape_a._with_num_row_partitions(num_row_partitions_a)
shape_b = DynamicRaggedShape.from_lengths(lengths_b)
if num_row_partitions_b is not None:
    shape_b = shape_b._with_num_row_partitions(num_row_partitions_b)
shape_e = DynamicRaggedShape.from_lengths(lengths_e)
if num_row_partitions_e is not None:
    shape_e = shape_e._with_num_row_partitions(num_row_partitions_e)

[actual, bc_a, bc_b
] = dynamic_ragged_shape.broadcast_dynamic_shape_extended(shape_a, shape_b)
[actual_rev, bc_b_rev, bc_a_rev
] = dynamic_ragged_shape.broadcast_dynamic_shape_extended(shape_b, shape_a)
self.assertShapeEq(actual, shape_e)
self.assertShapeEq(actual_rev, shape_e)

rt_a = ragged_array_ops.ragged_reshape(
    _lowest_primes(_num_elements_of_lengths(lengths_a)), shape_a)
bc_a_actual = bc_a.broadcast(rt_a)
bc_a_actual_rev = bc_a_rev.broadcast(rt_a)
bc_a_expected = dynamic_ragged_shape.broadcast_to(rt_a, shape_e)
self.assertAllEqual(bc_a_expected, bc_a_actual)
self.assertAllEqual(bc_a_expected, bc_a_actual_rev)

rt_b = ragged_array_ops.ragged_reshape(
    _lowest_primes(_num_elements_of_lengths(lengths_b)), shape_b)
bc_b_expected = dynamic_ragged_shape.broadcast_to(rt_b, shape_e)
bc_b_actual = bc_b.broadcast(rt_b)
bc_b_actual_rev = bc_b_rev.broadcast(rt_b)
self.assertAllEqual(bc_b_expected, bc_b_actual)
self.assertAllEqual(bc_b_expected, bc_b_actual_rev)
