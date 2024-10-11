# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
strings = [b"ab\xe2\x82\xac", b"\xf0\x90\x90\xb7"]  # U+10437
expected = [s.decode("UTF-8").encode("UTF-16-BE") for s in strings]

with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        strings,
        input_encoding="UTF-8",
        output_encoding="UTF-16-BE",
        replacement_char=ord(" "),
        replace_control_characters=False)
    values = self.evaluate(outputs)
    self.assertAllEqual(values, expected)
