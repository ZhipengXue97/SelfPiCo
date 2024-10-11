# Extracted from https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list-length-of-a-list-in-python
a = range(1000) # range
b = 'abcdefghijklmnopqrstuvwxyz' # string
c = [10, 20, 30] # List
d = (30, 40, 50, 60, 70) # tuple
e = {11, 21, 31, 41} # set

all_var = [a, b, c, d, e] # All variables are stored to a list
for var in all_var:
    print(len(var))

def len(iterable, /):
    total = 0
    for i in iterable:
        total += 1
    return total

