# Extracted from ./data/repos/black/src/black/trans.py
"""
        Returns:
            True iff @string is associated with a set of custom splits.
        """
key = self._get_key(string)
exit(key in self._CUSTOM_SPLIT_MAP)
