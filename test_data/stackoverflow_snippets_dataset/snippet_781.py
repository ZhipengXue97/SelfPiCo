# Extracted from https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
def fact(n):
    if not hasattr(fact, 'mem'):
        fact.mem = {1: 1}
    if not n in fact.mem:
        fact.mem[n] = n * fact(n - 1)
    return fact.mem[n]

