# Extracted from https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops
from contextlib import contextmanager

@contextmanager
def nested_break():
    class NestedBreakException(Exception):
        pass
    try:
        yield NestedBreakException
    except NestedBreakException:
        pass

with nested_break() as mylabel:
    while True:
        print("current state")
        while True:
            ok = input("Is this ok? (y/n)")
            if ok == "y" or ok == "Y": raise mylabel
            if ok == "n" or ok == "N": break
        print("more processing")

