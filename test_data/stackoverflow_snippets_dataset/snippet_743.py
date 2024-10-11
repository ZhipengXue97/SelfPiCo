# Extracted from https://stackoverflow.com/questions/533905/how-to-get-the-cartesian-product-of-multiple-lists
import itertools

somelists = [
   [1, 2, 3],
   ['a', 'b'],
   [4, 5]
]
lst = [i for i in itertools.product(*somelists)]

