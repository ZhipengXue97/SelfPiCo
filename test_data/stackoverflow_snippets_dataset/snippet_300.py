# Extracted from https://stackoverflow.com/questions/976882/shuffling-a-list-of-objects
#!/usr/bin/python3

import random

s=list(range(5))
random.shuffle(s) # << shuffle before print or assignment
print(s)

# print: [2, 4, 1, 3, 0]

