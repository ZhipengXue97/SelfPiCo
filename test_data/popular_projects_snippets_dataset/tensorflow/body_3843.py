# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/pad/ops_defs.py
shape = input_.shape.as_list()
for i in range(len(shape)):
    rdims = tf.raw_ops.OneHot(
        indices=i, depth=len(shape), on_value=True, off_value=False, axis=-1)
    left_padding_size = tf.raw_ops.GatherNd(params=paddings, indices=[i, 0])
    right_padding_size = tf.raw_ops.GatherNd(params=paddings, indices=[i, 1])

    split_outputs = tf.raw_ops.SplitV(
        value=input_,
        size_splits=[left_padding_size, -1, right_padding_size],
        axis=i,
        num_split=3)
    left_padding = split_outputs[0]
    core = split_outputs[1]
    right_padding = split_outputs[2]
    reversed_left_padding = tf.raw_ops.Reverse(tensor=left_padding, dims=rdims)
    reversed_right_padding = tf.raw_ops.Reverse(
        tensor=right_padding, dims=rdims)
    zero_like = tf.raw_ops.ZerosLike(x=core)
    left_offset, _ = tf.raw_ops.SplitV(
        value=zero_like,
        size_splits=[-1, left_padding_size],
        axis=i,
        num_split=2)
    right_offset, _ = tf.raw_ops.SplitV(
        value=zero_like,
        size_splits=[-1, right_padding_size],
        axis=i,
        num_split=2)

    if mode == 'REFLECT':
        from_left_padding = tf.raw_ops.Concat(
            concat_dim=i, values=[left_offset, reversed_left_padding])
        from_right_padding = tf.raw_ops.Concat(
            concat_dim=i, values=[reversed_right_padding, right_offset])
    else:
        from_left_padding = tf.raw_ops.Concat(
            concat_dim=i, values=[reversed_left_padding, left_offset])
        from_right_padding = tf.raw_ops.Concat(
            concat_dim=i, values=[right_offset, reversed_right_padding])
    input_ = tf.raw_ops.AddN(
        inputs=[from_left_padding, core, from_right_padding])

exit(input_)
