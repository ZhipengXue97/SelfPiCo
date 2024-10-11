# Extracted from https://stackoverflow.com/questions/1987694/how-do-i-print-the-full-numpy-array-without-truncation
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

