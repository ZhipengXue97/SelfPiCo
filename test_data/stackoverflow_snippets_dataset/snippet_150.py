# Extracted from https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
import operator
stats = {'a': 1000, 'b': 3000, 'c': 100}
max(stats.iteritems(), key=operator.itemgetter(1))[0]

import operator
stats = {'a': 1000, 'b': 3000, 'c': 100, 'd': 3000}
max(stats.iteritems(), key=operator.itemgetter(1))[0]
'b' 

max(stats.items(), key=operator.itemgetter(1))[0]
'b'

