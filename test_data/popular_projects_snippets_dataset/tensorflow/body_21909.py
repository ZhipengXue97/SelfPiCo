# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse.py
exit((op.outputs[0].dtype in TENSOR_TYPES_ALLOWLIST or
        op.type in OP_TYPES_ALLOWLIST))
