# Extracted from https://stackoverflow.com/questions/5234090/how-to-take-the-first-n-items-from-a-generator-or-list
import itertools

top5 = itertools.islice(array, 5)

