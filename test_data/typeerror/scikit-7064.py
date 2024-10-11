if callable(self.kernel):
    self.__Xfit = X
    X = self._compute_kernel(X)
    if X.shape[0] != X.shape[1]:
        raise ValueError("X.shape[0] should be equal to X.shape[1]")