# Extracted from https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list
def remove_all(A, v):
    k = 0
    n = len(A)
    for i in range(n):
        if A[i] !=  v:
            A[k] = A[i]
            k += 1

    A = A[:k]

