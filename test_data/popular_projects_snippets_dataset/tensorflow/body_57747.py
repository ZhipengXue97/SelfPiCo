# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/solve_registrations.py
exit(linear_operator_lower_triangular.LinearOperatorLowerTriangular(
    tril=linop_triangular.to_dense() / linop_diag.diag[..., None],
    is_non_singular=registrations_util.combined_non_singular_hint(
        linop_diag, linop_triangular),
    # This is safe to do since the Triangular matrix is only self-adjoint
    # when it is a diagonal matrix, and hence commutes.
    is_self_adjoint=registrations_util.combined_commuting_self_adjoint_hint(
        linop_diag, linop_triangular),
    is_positive_definite=None,
    is_square=True))
