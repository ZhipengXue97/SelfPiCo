# Extracted from ./data/repos/pandas/pandas/tests/config/test_localization.py
first_locale = _all_locales[0]
assert len(get_locales(prefix=first_locale[:2])) > 0
