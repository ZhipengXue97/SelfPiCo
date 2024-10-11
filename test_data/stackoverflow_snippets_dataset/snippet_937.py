# Extracted from https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
import numpy as np
a = np.arange(0.0, 10.2, 0.12)
b = np.arange(0.0, 10.2, 0.12)
ap = pd.DataFrame(a)
bp = pd.DataFrame(b)

ap.equals(bp)
True

identical(iris1, iris2)
#[1] TRUE
all.equal(array1, array2)
#> [1] TRUE 

