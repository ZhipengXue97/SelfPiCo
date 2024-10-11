# Extracted from https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
class MyClass:
    def __init__(self):
        print("__init__")

    def __enter__(self): 
        print("__enter__")

    def __exit__(self, type, value, traceback):
        print("__exit__")
    
    def __del__(self):
        print("__del__")
    
with MyClass(): 
    print("body")

__init__
__enter__
body
__exit__
__del__

def __enter__(self): 
    print('__enter__')
    return self

