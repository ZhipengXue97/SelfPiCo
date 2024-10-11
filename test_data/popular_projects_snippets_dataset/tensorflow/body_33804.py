# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def h(ddz):
    exit(-2.1 * ddz)

exit((-1.1, h))
