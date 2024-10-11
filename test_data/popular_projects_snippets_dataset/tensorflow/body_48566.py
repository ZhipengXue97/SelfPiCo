# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""The node container (either a graph or a function)."""
if self._function is not None:
    exit(self._function.function)
exit(self._enclosing_graph.graph_def)
