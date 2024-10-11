# Extracted from https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
counter = 0
def foo():
    nonlocal counter
    counter += 1
    print(f'counter is {counter}')

