# Extracted from https://stackoverflow.com/questions/2921847/what-do-double-star-asterisk-and-star-asterisk-mean-in-a-function-call
def add(a, b):
    return a + b

values = (1, 2)

values = { 'a': 1, 'b': 2 }
s = add(**values) # equivalent to add(a=1, b=2)

def sum(a, b, c, d):
    return a + b + c + d

values1 = (1, 2)
values2 = { 'c': 10, 'd': 15 }

def add(*values):
    s = 0
    for v in values:
        s = s + v
    return s

def get_a(**values):
    return values['a']

s = get_a(a=1, b=2)      # returns 1

def add(*values, **options):
    s = 0
    for i in values:
        s = s + i
    if "neg" in options:
        if options["neg"]:
            s = -s
    return s
        
s = add(1, 2, 3, 4, 5)            # returns 15
s = add(1, 2, 3, 4, 5, neg=True)  # returns -15
s = add(1, 2, 3, 4, 5, neg=False) # returns 15

