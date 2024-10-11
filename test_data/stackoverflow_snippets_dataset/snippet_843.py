# Extracted from https://stackoverflow.com/questions/1261875/what-does-nonlocal-do-in-python-3
def outer():
    def inner():
        def innermost():
            nonlocal x
            x = 3

        x = 2
        innermost()
        if x == 3: print('Inner x has been modified')

    x = 1
    inner()
    if x == 3: print('Outer x has been modified')

x = 0
outer()
if x == 3: print('Global x has been modified')

# Inner x has been modified

def outer():
    def inner():
        def innermost():
            nonlocal x
            x = 3

        innermost()

    x = 1
    inner()
    if x == 3: print('Outer x has been modified')

x = 0
outer()
if x == 3: print('Global x has been modified')

# Outer x has been modified

def outer():
    def inner():
        def innermost():
            nonlocal x
            x = 3

        innermost()

    inner()

x = 0
outer()
if x == 3: print('Global x has been modified')

# SyntaxError: no binding for nonlocal 'x' found

