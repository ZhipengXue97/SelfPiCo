# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
expected_source = parser.unparse(expected_node, indentation='  ')
expected_str = textwrap.dedent(expected_source).strip()
got_source = parser.unparse(node, indentation='  ')
got_str = textwrap.dedent(got_source).strip()
self.assertEqual(expected_str, got_str, msg=msg)
