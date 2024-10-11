# Extracted from https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
a = np.array([9, 4, 4, 3, 3, 9, 0, 4, 6, 0])
a
array([9, 4, 4, 3, 3, 9, 0, 4, 6, 0])

ind = np.argpartition(a, -4)[-4:]
ind
array([1, 5, 8, 0])

top4 = a[ind]
top4
array([4, 9, 6, 9])

ind[np.argsort(a[ind])]
array([1, 8, 5, 0])

