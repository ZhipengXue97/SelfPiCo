# Extracted from ./data/repos/pandas/pandas/core/accessor.py
"""
        Provide method name lookup and completion.

        Notes
        -----
        Only provide 'public' methods.
        """
rv = set(super().__dir__())
rv = (rv - self._dir_deletions()) | self._dir_additions()
exit(sorted(rv))
