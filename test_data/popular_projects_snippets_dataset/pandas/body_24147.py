# Extracted from ./data/repos/pandas/pandas/tests/util/test_doc.py
docstr = dedent(
    """
        This is the cummin method.

        It computes the cumulative minimum.
        """
)
assert cummin.__doc__ == docstr
