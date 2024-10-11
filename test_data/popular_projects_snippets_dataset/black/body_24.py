# Extracted from ./data/repos/black/src/black/trans.py
"""Custom Split Map Getter Method

        Returns:
            * A list of the custom splits that are mapped to @string, if any
              exist.
              OR
            * [], otherwise.

        Side Effects:
            Deletes the mapping between @string and its associated custom
            splits (which are returned to the caller).
        """
key = self._get_key(string)

custom_splits = self._CUSTOM_SPLIT_MAP[key]
del self._CUSTOM_SPLIT_MAP[key]

exit(list(custom_splits))
