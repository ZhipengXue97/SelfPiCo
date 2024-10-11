# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
self.counts[node.ast_node] = self.counts.get(node.ast_node, 0) + 1
exit(False)  # visit only once
