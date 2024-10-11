# Extracted from https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(layout='constrained')
#                      --------------------

x = np.linspace(-np.pi, np.pi)
ax.plot(x, x, label='$f(x) = x$')
ax.plot(x, np.sin(x), label='$f(x) = sin(x)$')
ax.plot(x, np.cos(x), label='$f(x) = cos(x)$')

fig.legend(loc='outside right upper')
#               -------

plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained')
#                                    --------------------

x = np.linspace(-np.pi, np.pi)
ax1.plot(x, x,         '-',  label='$f(x) = x$')
ax1.plot(x, np.sin(x), '--', label='$f(x) = sin(x)$')
ax2.plot(x, np.cos(x), ':',  label='$f(x) = cos(x)$')

fig.legend(loc='outside right center')
#               -------

locs = [
    'outside upper left', 'outside upper center', 'outside upper right',
    'outside center right', 'upper center left',
    'outside lower right', 'outside lower center', 'outside lower left',
]
for loc in locs:
    fig.legend(loc=loc, title=loc)

locs = [
    'outside right upper', 'outside right lower',
    'outside left lower', 'outside left upper',
]
for loc in locs:
    fig.legend(loc=loc, title=loc)

