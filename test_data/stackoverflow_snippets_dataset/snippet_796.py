# Extracted from https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
import numpy as np
import bisect
xarr = np.random.rand(int(1e7))

srt_ind = xarr.argsort()
xar = xarr.copy()[srt_ind]
xlist = xar.tolist()
bisect.bisect_left(xlist, 0.3)

np.searchsorted(xar, 0.3, side="left")

randpts = np.random.rand(1000)
np.searchsorted(xar, randpts, side="left")

