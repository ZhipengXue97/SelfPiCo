# Extracted from https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
for item in sequence:
    do_something(item)

item = None
while sequence.hasnext():
    item = sequence.next()
    do_something(item)

