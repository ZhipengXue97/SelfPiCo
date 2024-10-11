# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Disable further changes to the current settings.

        After calling this method, the present state of the settings will become
        immutable. Trying to change values through the :meth:`~set` method and
        its variants won't be possible and will be alerted.
        """
self.frozen = True
