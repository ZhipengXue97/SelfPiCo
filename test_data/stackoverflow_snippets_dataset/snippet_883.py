# Extracted from https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
# Python list with append()
np.mean(timeit.repeat(setup="a = []", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
# 0.054 +/- 0.025 msec

# Python array with append()
np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
# 0.104 +/- 0.025 msec

# Numpy array with append()
np.mean(timeit.repeat(setup="import numpy as np; a = np.array([])", stmt="np.append(a, [1.0])", number=1000, repeat=5000)) * 1000
# 5.183 +/- 0.950 msec

# Python list using +=
np.mean(timeit.repeat(setup="a = []", stmt="a += [1.0]", number=1000, repeat=5000)) * 1000
# 0.062 +/- 0.021 msec

# Python array using += 
np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a += array.array('f', [1.0]) ", number=1000, repeat=5000)) * 1000
# 0.289 +/- 0.043 msec

# Python list using extend()
np.mean(timeit.repeat(setup="a = []", stmt="a.extend([1.0])", number=1000, repeat=5000)) * 1000
# 0.083 +/- 0.020 msec

# Python array using extend()
np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a.extend([1.0]) ", number=1000, repeat=5000)) * 1000
# 0.169 +/- 0.034

