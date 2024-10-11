# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator.py
# pylint: disable=line-too-long
"""Parse a debug tensor name in a to-be-evaluated expression.

  Args:
    debug_tensor_name: name of the debug tensor, with or without
      device name as a prefix, with or without debug op, with or
      without '[<exec_index>]' as a suffix.
      E.g., without device name prefix, without debug op suffix:
        "hidden_0/MatMul:0"
      E.g., with device name prefix:
        "/job:worker/replica:0/task:1/gpu:0:hidden_0/MatMul:0"
      E.g., with debug op suffix:
        "hidden_0/MatMul:0:DebugNumericSummary"
      E.g., with device name prefix and debug op suffix:
        "/job:worker/replica:0/task:1/gpu:0:hidden_0/MatMul:0:DebugNumericSummary"
      E.g., with device name prefix, debug op and an exec index:
        "/job:worker/replica:0/task:1/gpu:0:hidden_0/MatMul:0:DebugNumericSummary[1]"

  Returns:
    device_name: If device name prefix exists, the device name; otherwise,
      `None`.
    node_name: Name of the node.
    output_slot: Output slot index as an `int`.
    debug_op: If the debug op suffix exists, the debug op name; otherwise,
      `None`.
    exec_index: Execution index (applicable to cases in which a debug tensor
      is computed multiple times in a `tf.Session.run` call, e.g., due to
      `tf.while_loop`). If the exec_index suffix does not exist, this value
      defaults to `0`.

  Raises:
    ValueError: If the input `debug_tensor_name` is malformed.
  """
# pylint: enable=line-too-long
device_prefix_match = re.match(_DEVICE_NAME_PREFIX_PATTERN, debug_tensor_name)
if device_prefix_match:
    device_name = debug_tensor_name[
        device_prefix_match.start() : device_prefix_match.end() - 1]
    debug_tensor_name = debug_tensor_name[device_prefix_match.end():]
else:
    device_name = None

split_items = debug_tensor_name.split(":")
if len(split_items) not in (2, 3):
    raise ValueError(
        "The debug tensor name in the to-be-evaluated expression is malformed: "
        "'%s'" % debug_tensor_name)
    # TODO(cais): Provide examples of good debug tensor names in the error
    # message.

exec_index_match = re.search(_EXEC_INDEX_SUFFIX_PATTERN, split_items[-1])
if exec_index_match:
    exec_index = int(split_items[-1][
        exec_index_match.start() + 1 : exec_index_match.end() - 1])
    split_items[-1] = split_items[-1][:exec_index_match.start()]
else:
    exec_index = 0

if len(split_items) == 2:
    node_name = split_items[0]
    output_slot = int(split_items[1])
    debug_op = _DEFAULT_DEBUG_OP
else:
    split_items = debug_tensor_name.split(":")
    node_name = split_items[0]
    output_slot = int(split_items[1])
    debug_op = split_items[2]

exit((device_name, node_name, output_slot, debug_op, exec_index))
