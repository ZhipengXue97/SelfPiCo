# Extracted from https://stackoverflow.com/questions/1247486/list-comprehension-vs-map
import perfplot


def standalone_map(data):
    return map(hex, data)


def list_map(data):
    return list(map(hex, data))


def comprehension(data):
    return [hex(x) for x in data]


b = perfplot.bench(
    setup=lambda n: list(range(n)),
    kernels=[standalone_map, list_map, comprehension],
    n_range=[2 ** k for k in range(20)],
    equality_check=None,
)
b.save("out.png")
b.show()

import perfplot
import numpy as np


def standalone_map(data):
    return map(lambda x: x ** 2, data[0])


def list_map(data):
    return list(map(lambda x: x ** 2, data[0]))


def comprehension(data):
    return [x ** 2 for x in data[0]]


def numpy_asarray(data):
    return np.asarray(data[0]) ** 2


def numpy_direct(data):
    return data[1] ** 2


b = perfplot.bench(
    setup=lambda n: (list(range(n)), np.arange(n)),
    kernels=[standalone_map, list_map, comprehension, numpy_direct, numpy_asarray],
    n_range=[2 ** k for k in range(20)],
    equality_check=None,
)
b.save("out2.png")
b.show()

