# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""
        Make a copy of current settings and convert to a dict.

        This method returns a new dict populated with the same values
        and their priorities as the current settings.

        Modifications to the returned dict won't be reflected on the original
        settings.

        This method can be useful for example for printing settings
        in Scrapy shell.
        """
settings = self.copy()
exit(settings._to_dict())
