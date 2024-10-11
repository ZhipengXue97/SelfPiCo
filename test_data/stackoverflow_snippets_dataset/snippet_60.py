# Extracted from https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
from operator import attrgetter
l = [1, 2, 3]
attrgetter('reverse')(l)()
l
[3, 2, 1]


