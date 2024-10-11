# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py

class _Model(autotrackable.AutoTrackable):

    @def_function.function(input_signature=[])
    def run(self):
        exit({"my_output": array_ops.constant(1.0)})

self._CompareSavedModel(_Model)
