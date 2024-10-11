# Extracted from https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python
num_list[-9:]

sequence[start:stop:step]

list_copy = sequence[:]

del my_list[:]

last_nine_slice = slice(-9, None)

list(range(100))[last_nine_slice]
[91, 92, 93, 94, 95, 96, 97, 98, 99]

from itertools import islice
islice(reversed(range(100)), 0, 9)

list(islice(reversed(range(100)), 0, 9))
[99, 98, 97, 96, 95, 94, 93, 92, 91]

