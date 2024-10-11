# Extracted from https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python
x = x ^ y
y = y ^ x
x = x ^ y

x ^= y
y ^= x
x ^= y

w = x
x = y
y = w
del w

x, y = y, x

