# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/mlir/mlir_test.py
"""Tests the basic flow of `experimental_tflite_to_tosa_bytecode`."""
filename = os.path.join(self.get_temp_dir(), "multi_add_tosa.mlirbc")
experimental_tflite_to_tosa_bytecode(
    resource_loader.get_path_to_datafile("multi_add.tflite"), filename
)
with open(filename, mode="rb") as f:
    chunk = f.read(4)
# Just verify output is bytecode.
self.assertEqual(b"ML\xefR", chunk)
