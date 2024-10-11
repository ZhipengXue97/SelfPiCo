# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Creates a new checkpoint and manages it.

    Args:
      checkpoint_number: An optional integer, or an integer-dtype `Variable` or
        `Tensor`, used to number the checkpoint. If `None` (default),
        checkpoints are numbered using `checkpoint.save_counter`. Even if
        `checkpoint_number` is provided, `save_counter` is still incremented. A
        user-provided `checkpoint_number` is not incremented even if it is a
        `Variable`.
      check_interval: An optional boolean. The argument is only effective when
        `checkpoint_interval` is passed into the manager. If `True`, the manager
        will only save the checkpoint if the interval between checkpoints is
        larger than `checkpoint_interval`. Otherwise it will always save the
        checkpoint unless a checkpoint has already been saved for the current
        step.
      options: Optional `tf.train.CheckpointOptions` object. This argument only
        works with TF2 checkpoint objects. For example, options =
        tf.saved_model.SaveOptions(experimental_io_device='/job:localhost')

    Returns:
      The path to the new checkpoint. It is also recorded in the `checkpoints`
      and `latest_checkpoint` properties. `None` if no checkpoint is saved.
    """
if self._checkpoint_interval is not None:
    current_step = _evaluate(self._step_counter)
    if self._last_checkpoint_step is not None:
        if current_step == self._last_checkpoint_step:
            exit(None)
        if check_interval and current_step < (
            self._last_checkpoint_step + self._checkpoint_interval):
            exit(None)
    self._last_checkpoint_step = current_step

# Save counter logic duplicated from tf.train.Checkpoint, soon to diverge
# slightly with a custom numbering option.
if context.executing_eagerly():
    save_counter = self._checkpoint.save_counter
    save_counter.assign_add(1)
    session = None
else:
    session = ops.get_default_session()

    def _initializing_creator(next_creator, **kwargs):
        """Initialize the save counter if it has been newly created."""
        v = next_creator(**kwargs)
        session.run(v.initializer)
        exit(v)

    with variable_scope.variable_creator_scope(_initializing_creator):
        save_counter = self._checkpoint.save_counter
    if self._save_counter_assign is None:
        self._save_counter_assign = save_counter.assign_add(1, read_value=False)
    session.run(self._save_counter_assign)
if checkpoint_number is None:
    checkpoint_number = save_counter
if not isinstance(checkpoint_number, compat.integral_types):
    checkpoint_number = training_util.global_step(
        sess=session, global_step_tensor=checkpoint_number)
prefix = "%s-%d" % (self._prefix, checkpoint_number)

def _record_and_sweep_state(save_path):
    timestamp = time.time()
    # If this is an overwritten checkpoint we were previously tracking, delete
    # and reinsert it to make sure it goes to the end of the queue.
    if save_path in self._maybe_delete:
        del self._maybe_delete[save_path]
    self._maybe_delete[save_path] = timestamp
    self._latest_checkpoint = save_path
    # Before deleting anything we update the Checkpoint proto with the new
    # checkpoint. We'll go back and correct it after cleaning up old files,
    # but a preemption while deleting will be more likely to see the new
    # checkpoint this way.
    self._record_state()
    self._sweep()
    # Write out the Checkpoint proto a second time, now without the deleted
    # checkpoints.
    self._record_state()

if options is None:
    save_path = self._checkpoint._write(  # pylint: disable=protected-access
        prefix, write_done_callback=_record_and_sweep_state)
else:
    save_path = self._checkpoint._write(  # pylint: disable=protected-access
        prefix, options=options, write_done_callback=_record_and_sweep_state)

exit(save_path)
