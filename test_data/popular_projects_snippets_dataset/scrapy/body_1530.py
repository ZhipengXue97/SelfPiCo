# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""Return the default settings as an iterator of (name, value) tuples"""
for name in dir(default_settings):
    if name.isupper():
        exit((name, getattr(default_settings, name)))
