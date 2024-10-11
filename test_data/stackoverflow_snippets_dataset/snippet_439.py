# Extracted from https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib
for i in range(5):
    fig = plot_figure()
    plt.close(fig)
# This returns a list with all figure numbers available
print(plt.get_fignums())

for i in range(5):
    fig = plot_figure()
    fig.clf()
# This returns a list with all figure numbers available
print(plt.get_fignums())

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1000)
y = np.sin(x)

for i in range(5):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    plt.close(fig)

print(plt.get_fignums())

for i in range(5):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    fig.clf()

print(plt.get_fignums())

