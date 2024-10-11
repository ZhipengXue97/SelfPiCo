# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
if values is not None:
    exit([type_fn(val) for val in values.split(",") if val])
exit(None)
