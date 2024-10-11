# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Replace already existing capture."""
self._function_captures.add_or_replace(
    key=id(tensor),
    external=tensor,
    internal=placeholder,
    is_by_ref=False)
