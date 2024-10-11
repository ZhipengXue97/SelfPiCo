# Extracted from https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops
def foo():
    for x in range(10):
        for y in range(10):
            print(x*y)
            if x*y > 50:
                return
foo()

def your_outer_func():
    ...
    def inner_func():
        for x in range(10):
            for y in range(10):
                print(x*y)
                if x*y > 50:
                    return
    inner_func()
    ...

