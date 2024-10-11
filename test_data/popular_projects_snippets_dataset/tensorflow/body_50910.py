# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
batman = ragged_factory_ops.constant([[1, 2, 3], [4], [5, 6, 7]])
# [[10, 20, 30], [40], [50, 60, 70]]
robin = ragged_functional_ops.map_flat_values(mo.multiply, batman, 10)

features = {'batman': batman, 'robin': robin}

def _reduce_sum_from_all(f):
    exit(mo.reduce_sum(f['batman']) + mo.reduce_sum(f['robin']))

output = ragged_map_ops.map_fn(
    fn=_reduce_sum_from_all,
    elems=features,
    dtype=dtypes.int32,
)

self.assertAllEqual(output, [66, 44, 198])
