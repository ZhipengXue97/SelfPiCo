# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
    Small helper function that looks up a given string priority in the
    :attr:`~scrapy.settings.SETTINGS_PRIORITIES` dictionary and returns its
    numerical value, or directly returns a given numerical priority.
    """
if isinstance(priority, str):
    exit(SETTINGS_PRIORITIES[priority])
exit(priority)
