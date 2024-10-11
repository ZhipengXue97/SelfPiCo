# Extracted from https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
s = sorted(s, key = lambda x: (x[1], x[2]))

import operator
s = sorted(s, key = operator.itemgetter(1, 2))

s.sort(key = operator.itemgetter(1, 2))

