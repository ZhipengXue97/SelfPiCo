# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
bad_string = b"\x00\xff"
with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        bad_string,
        input_encoding="UTF-8",
        output_encoding="UTF-8",
        errors="ignore")
    values = self.evaluate(outputs)
    self.assertAllEqual(values, b"\x00")
