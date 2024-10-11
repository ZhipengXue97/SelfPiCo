# Extracted from https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
import numpy as np
def forward(xi, W1, b1, W2, b2):
    z1 = W1 @ xi + b1
    a1 = sigma(z1)
    z2 = W2 @ a1 + b2
    return z2, a1

