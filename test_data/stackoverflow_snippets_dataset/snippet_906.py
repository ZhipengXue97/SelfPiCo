# Extracted from https://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u
np.matrix("1, 1+1j, 0; 0, 1j, 0; 0, 0, 1")

matrix([[1.+0.j, 1.+1.j, 0.+0.j],
        [0.+0.j, 0.+1.j, 0.+0.j],
        [0.+0.j, 0.+0.j, 1.+0.j]])

np.array("1, 1+1j, 0; 0, 1j, 0; 0, 0, 1")

array('1, 1+1j, 0; 0, 1j, 0; 0, 0, 1', dtype='<U29')

