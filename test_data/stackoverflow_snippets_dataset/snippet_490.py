# Extracted from https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(1500)

