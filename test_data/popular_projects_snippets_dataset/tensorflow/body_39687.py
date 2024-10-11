# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = [
    example(features=features({
        "val": bytes_feature([b"a", b"b"]),
        "idx": int64_feature([0, 3])
    })), example(features=features({
        "val": bytes_feature([b"c", b"d"]),
        "idx": int64_feature([7, 1])
    }))
]

expected_outputs = [{
    "idx": (np.array([[0], [1]], dtype=np.int64),
            np.array([0, 3], dtype=np.int64), np.array([2],
                                                       dtype=np.int64)),
    "sp": (np.array([[0], [3]], dtype=np.int64),
           np.array(["a", "b"], dtype=bytes), np.array(
               [13], dtype=np.int64))
},
                    {
                        "idx": (np.array([[0], [1]], dtype=np.int64),
                                np.array([7, 1], dtype=np.int64),
                                np.array([2], dtype=np.int64)),
                        "sp": (np.array([[1], [7]], dtype=np.int64),
                               np.array(["d", "c"], dtype=bytes),
                               np.array([13], dtype=np.int64))
                    }]

for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            "idx":
                parsing_ops.VarLenFeature(dtypes.int64),
            "sp":
                parsing_ops.SparseFeature(["idx"], "val", dtypes.string, [13]
                                         ),
        }
    }, expected_output)
