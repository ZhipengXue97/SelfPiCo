# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    sequence_example(
        context=features({"a": float_feature([3, 4])}),
        feature_lists=feature_lists({
            "b": feature_list([float_feature([5]),
                               float_feature([3])]),
            "c": feature_list([int64_feature([6, 7, 8, 9])])
        })),
    sequence_example(
        context=features({"a": float_feature([9])}),
        feature_lists=feature_lists({
            "b": feature_list([]),
            "c": feature_list([int64_feature([]),
                               int64_feature([1, 2, 3])])
        })),
    sequence_example(
        feature_lists=feature_lists({
            "b":
                feature_list([
                    float_feature([1]),
                    float_feature([1, 2]),
                    float_feature([1, 2, 3])
                ])
        })),
    sequence_example(
        context=features({"a": feature()}),
        feature_lists=feature_lists({
            "b": feature_list([feature()]),
            "c": feature_list([int64_feature([3, 3, 3])])
        }))
]
serialized = [m.SerializeToString() for m in original]

context_features = {"a": parsing_ops.RaggedFeature(dtype=dtypes.float32)}
sequence_features = {
    "b":
        parsing_ops.RaggedFeature(dtype=dtypes.float32),
    "c":
        parsing_ops.RaggedFeature(
            dtype=dtypes.int64, row_splits_dtype=dtypes.int64)
}

expected_a = ragged_factory_ops.constant([[3, 4], [9], [], []],
                                         dtype=dtypes.float32,
                                         row_splits_dtype=dtypes.int32)
expected_b = ragged_factory_ops.constant(
    [[[5], [3]], [], [[1], [1, 2], [1, 2, 3]], [[]]],
    dtype=dtypes.float32,
    row_splits_dtype=dtypes.int32)
expected_c = ragged_factory_ops.constant(
    [[[6, 7, 8, 9]], [[], [1, 2, 3]], [], [[3, 3, 3]]],
    dtype=dtypes.int64,
    row_splits_dtype=dtypes.int64)

expected_context_output = dict(a=expected_a)
expected_feature_list_output = dict(b=expected_b, c=expected_c)

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "context_features": context_features,
        "sequence_features": sequence_features,
    },
    expected_context_output,
    expected_feature_list_output,
    batch=True)

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized)[0],
        "context_features": context_features,
        "sequence_features": sequence_features,
    },
    expected_context_values={"a": [3, 4]},
    expected_feat_list_values={
        "b": [[5], [3]],
        "c": [[6, 7, 8, 9]]
    },
    batch=False)

# Test with a larger batch of examples.
batch_serialized = serialized * 64
batch_context_expected_out = {
    "a": ragged_concat_ops.concat([expected_a] * 64, axis=0)
}
batch_feature_list_expected_out = {
    "b": ragged_concat_ops.concat([expected_b] * 64, axis=0),
    "c": ragged_concat_ops.concat([expected_c] * 64, axis=0)
}
self._test(
    {
        "serialized": ops.convert_to_tensor(batch_serialized),
        "context_features": context_features,
        "sequence_features": sequence_features,
    },
    batch_context_expected_out,
    batch_feature_list_expected_out,
    batch=True)
