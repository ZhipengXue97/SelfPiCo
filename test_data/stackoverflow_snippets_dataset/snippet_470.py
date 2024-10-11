# Extracted from https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
import operator
min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
max_index, max_value = max(enumerate(values), key=operator.itemgetter(1))

