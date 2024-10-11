# Extracted from ./data/repos/black/src/black/trans.py
"""Custom Split Map Setter Method

        Side Effects:
            Adds a mapping from @string to the custom splits @custom_splits.
        """
key = self._get_key(string)
self._CUSTOM_SPLIT_MAP[key] = tuple(custom_splits)
