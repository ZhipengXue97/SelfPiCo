if accept_sparse is False:
    raise TypeError('A sparse matrix was passed, but dense '
                    'data is required. Use X.toarray() to '
                    'convert to a dense numpy array.')