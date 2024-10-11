X = np.atleast_2d(X)
dists = squareform(pdist(X, metric='sqeuclidean'))
tmp = dists / (2 * self.alpha * self.length_scale ** 2)
base = (1 + tmp)
K = base ** -self.alpha