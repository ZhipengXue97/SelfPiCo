# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
mlir_code = tfr_gen(sys.modules[__name__], '_tfr_temp', [test_ops])
mlir_code_exp = r"""
      CHECK-LABEL: tfr.func @tf__test_identity_n_op(%x: !tfr.tensor_list) -> (!tfr.tensor_list)

      CHECK-LABEL: tfr.func @tf__test_identity_op(%x: !tfr.tensor) -> (!tfr.tensor) {
      CHECK-NEXT:   %[[list:.*]] = "tfr.build_list"(%x) : (!tfr.tensor) -> !tfr.tensor_list
      CHECK-NEXT:   %[[call:.*]] = tfr.call @tf__test_identity_n_op(%[[list]]) : (!tfr.tensor_list)
    """
self._check_code(mlir_code, mlir_code_exp)
