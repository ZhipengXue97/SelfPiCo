# Extracted from https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
import itertools
import timeit
big_list = [[0]*1000 for i in range(1000)]
timeit.repeat(lambda: list(itertools.chain.from_iterable(big_list)), number=100)
timeit.repeat(lambda: list(itertools.chain(*big_list)), number=100)
timeit.repeat(lambda: (lambda b: map(b.extend, big_list))([]), number=100)
timeit.repeat(lambda: [el for list_ in big_list for el in list_], number=100)
[100*x for x in timeit.repeat(lambda: sum(big_list, []), number=1)]

import itertools
import timeit
big_list = [[0]*1000 for i in range(1000)]
timeit.repeat(lambda: list(itertools.chain.from_iterable(big_list)), number=100)
[3.016212113769325, 3.0148865239060227, 3.0126415732791028]
timeit.repeat(lambda: list(itertools.chain(*big_list)), number=100)
[3.019953987082083, 3.528754223385439, 3.02181439266457]
timeit.repeat(lambda: (lambda b: map(b.extend, big_list))([]), number=100)
[1.812084445152557, 1.7702404451095965, 1.7722977998725362]
timeit.repeat(lambda: [el for list_ in big_list for el in list_], number=100)
[5.409658160700605, 5.477502077679354, 5.444318360412744]
[100*x for x in timeit.repeat(lambda: sum(big_list, []), number=1)]
[399.27587954973444, 400.9240571138051, 403.7521153804846]

