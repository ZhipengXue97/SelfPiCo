# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""Update map location for tag with file position"""
assert self.handles.handle is not None
self._map[tag] = self.handles.handle.tell()
