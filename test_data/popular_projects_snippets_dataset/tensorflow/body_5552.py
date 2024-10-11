# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
for align in alignment_list:
    for mat, tests in all_tests(align):
        for diag_index, (solution, _) in tests.items():
            self._assertOpOutputMatchesExpected(
                {
                    "input": mat,
                    "k": diag_index,
                    "align": align
                }, solution)
