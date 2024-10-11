# Extracted from https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehensions
from itertools import islice

def slice_and_continue(sequence):
    ret = []
    seq_i = iter(sequence) #create an iterator from the list

    seq_slice = islice(seq_i,3) #take first 3 elements and print
    for x in seq_slice: print(x),

    for x in seq_i: print(x**2), #square the rest of the numbers

slice_and_continue([1,2,3,4,5])

