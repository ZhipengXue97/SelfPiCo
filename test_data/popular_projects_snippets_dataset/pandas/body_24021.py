# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
expected_category, extra_category = pair_different_warnings
with tm.assert_produces_warning(expected_category, raise_on_extra_warnings=False):
    warnings.warn("Expected warning", expected_category)
    warnings.warn("Unexpected warning OK", extra_category)
