# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
exit([
    e.output_name
    for e in self._training_endpoints
    if e.has_feedable_training_target()
])
