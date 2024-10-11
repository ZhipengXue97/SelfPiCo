# Extracted from https://stackoverflow.com/questions/1966207/convert-numpy-array-to-python-list
c = np.array([[1,2,3],[4,5,6]])

c.ravel()
#>> array([1, 2, 3, 4, 5, 6])

# or
c.ravel().tolist()
#>> [1, 2, 3, 4, 5, 6]

