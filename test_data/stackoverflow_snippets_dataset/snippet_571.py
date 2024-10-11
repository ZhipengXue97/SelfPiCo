# Extracted from https://stackoverflow.com/questions/6618515/sorting-list-according-to-corresponding-values-from-a-parallel-list
X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
Y = [ 0,   1,   1,   0,   1,   2,   2,   0,   1 ]

# Zip (decorate), sort and unzip (undecorate).
# Converting to list to script the output and extract X
list(zip(*(sorted(zip(Y,X)))))[1]                                                                                                                       
# Results in: ('a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g')

import operator    

# Sort by Y (1) and extract X [0]
list(zip(*sorted(zip(X,Y), key=operator.itemgetter(1))))[0]                                                                                                 
# Results in: ('a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g')

